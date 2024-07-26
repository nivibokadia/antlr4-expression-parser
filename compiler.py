import sys
from antlr4 import *
from ExpressionLexer import ExpressionLexer
from ExpressionParser import ExpressionParser
from ExpressionVisitor import ExpressionVisitor

class Compiler(ExpressionVisitor):
    def __init__(self):
        self.bytecode = []
        self.symbol_table = {}
        self.functions = {}
        self.next_var_address = 0
        self.labels = {}
        self.label_count = 0
        self.current_function = None

    def new_label(self):
        label = f"label_{self.label_count}"
        self.label_count += 1
        return label

    def visitProgram(self, ctx):
        for stmt in ctx.statement():
            self.visit(stmt)
            
    def visitPrintStmt(self, ctx):
        expr_type = self.visit(ctx.expression())
        self.bytecode.append(('PRINT',))
        return None

    def visitArrayInitializer(self, ctx):
        elements = ctx.expression()
        self.bytecode.append(('CREATE_ARRAY', len(elements)))
        for expr in elements:
            self.visit(expr)
            self.bytecode.append(('ARRAY_PUSH',))

    def visitArrayAccessExpr(self, ctx):
        array_name = ctx.IDENTIFIER().getText()
        if array_name not in self.symbol_table:
            raise Exception(f"Undefined array: {array_name}")
        array_address, array_type = self.symbol_table[array_name]
        if not array_type.endswith('[]'):
            raise Exception(f"Variable {array_name} is not an array")
        self.bytecode.append(('LOAD_ARRAY', str(array_address)))
        self.visit(ctx.expression())
        self.bytecode.append(('ARRAY_LOAD',))

    def visitArrayLengthExpr(self, ctx):
        array_name = ctx.IDENTIFIER().getText()
        if array_name not in self.symbol_table:
            raise Exception(f"Undefined array: {array_name}")
        array_address = self.symbol_table[array_name][0]
        self.bytecode.append(('LOAD', array_address))
        self.bytecode.append(('ARRAY_LENGTH',))
        
    def visitArrayPushStmt(self, ctx):
        array_name = ctx.IDENTIFIER().getText()
        if array_name not in self.symbol_table:
            raise Exception(f"Undefined array: {array_name}")
        array_address = self.symbol_table[array_name][0]
        self.bytecode.append(('LOAD_ARRAY', str(array_address)))
        self.visit(ctx.expression())
        self.bytecode.append(('ARRAY_PUSH',))
        self.bytecode.append(('STORE_ARRAY', str(array_address), self.symbol_table[array_name][1]))
        
    def visitArrayPopStmt(self, ctx):
        array_name = ctx.IDENTIFIER().getText()
        if array_name not in self.symbol_table:
            raise Exception(f"Undefined array: {array_name}")
        array_address = self.symbol_table[array_name][0]
        self.bytecode.append(('LOAD_ARRAY', str(array_address)))
        self.bytecode.append(('ARRAY_POP',))
        self.bytecode.append(('STORE_ARRAY', str(array_address), self.symbol_table[array_name][1]))

    def visitLiteral(self, node):
        if isinstance(node.value, int):
            self.bytecode.append(('PUSH', str(node.value)))
        elif isinstance(node.value, float):
            self.bytecode.append(('PUSH', str(node.value)))
        elif isinstance(node.value, str):
            self.bytecode.append(('PUSH', node.value))
        elif isinstance(node.value, bool):
            self.bytecode.append(('PUSH', str(int(node.value))))
    
    def visitDeclareStmt(self, ctx):
        var_name = ctx.IDENTIFIER().getText()
        var_type = ctx.TYPE().getText()
        is_array = var_type.endswith('[]')
        if var_name not in self.symbol_table:
            self.symbol_table[var_name] = (self.next_var_address, var_type)
            self.next_var_address += 1
        elif var_name in self.symbol_table:
            raise Exception("Variable with the same name already defined")
        if ctx.arrayInitializer():
            if not is_array:
                raise Exception(f"Cannot initialize non-array variable {var_name} with array")
            self.visit(ctx.arrayInitializer())
            self.bytecode.append(('STORE_ARRAY', self.symbol_table[var_name][0], var_type))
        elif ctx.expression():
            self.visit(ctx.expression())
            if is_array:
                self.bytecode.append(('STORE_ARRAY', self.symbol_table[var_name][0], var_type))
            else:
                self.bytecode.append(('STORE', self.symbol_table[var_name][0], var_type))

    def visitStringExpr(self, ctx):
        value = ctx.STRING().getText()
        self.bytecode.append(('PUSH', value))

    def getVariableAddress(self, var_name):
        if var_name not in self.symbol_table:
            raise Exception(f"Undefined variable: {var_name}")
        return self.symbol_table[var_name][0]
    
    def visitGotoStmt(self, ctx):
        label = ctx.IDENTIFIER().getText()
        self.bytecode.append(('JMP', label))

    def visitLabeledStmt(self, ctx):
        label = ctx.IDENTIFIER().getText()
        self.bytecode.append(('LABEL', label))
        self.visit(ctx.statement())

    def visitForStmt(self, ctx):
        start_label = self.new_label()
        end_label = self.new_label()
        update_label = self.new_label()
        if ctx.forInit():
            self.visit(ctx.forInit())
        self.bytecode.append(('LABEL', start_label))
        if ctx.expression():
            self.visit(ctx.expression())
            self.bytecode.append(('JMP_IF_FALSE', end_label))
        self.visit(ctx.block())
        self.bytecode.append(('LABEL', update_label))
        if ctx.forUpdate():
            self.visit(ctx.forUpdate())
        self.bytecode.append(('JMP', start_label))
        self.bytecode.append(('LABEL', end_label))

    def visitForInit(self, ctx):
        if ctx.TYPE():
            var_type = ctx.TYPE().getText()
            var_name = ctx.IDENTIFIER().getText()
            self.symbol_table[var_name] = (self.next_var_address, var_type)
            self.next_var_address += 1

        self.visit(ctx.expression())
        address = self.getVariableAddress(ctx.IDENTIFIER().getText())
        self.bytecode.append(('STORE', str(address), var_type if ctx.TYPE() else 'unknown'))

    def visitForUpdate(self, ctx):
        var_name = ctx.IDENTIFIER().getText()
        address = self.getVariableAddress(var_name)

        if ctx.getChild(1).getText() in ['++', '--']:
            op = 'INC' if ctx.getChild(1).getText() == '++' else 'DEC'
            self.bytecode.append((op, str(address)))
        elif ctx.getChild(1).getText() == '+=':
            self.visit(ctx.expression())
            self.bytecode.append(('LOAD', str(address)))
            self.bytecode.append(('ADD',))
            self.bytecode.append(('STORE', str(address)))
        else:  #'='case
            self.visit(ctx.expression())
            self.bytecode.append(('STORE', str(address)))
            
    def visitIncDecStmt(self, ctx):
        var_name = ctx.IDENTIFIER().getText()
        if var_name not in self.symbol_table:
            raise Exception(f"Undefined variable: {var_name}")
        address = self.symbol_table[var_name][0]
        op = 'INC' if ctx.getChild(1).getText() == '++' else 'DEC'
        self.bytecode.append((op, str(address)))

    def visitAssignStmt(self, ctx):
        var_name = ctx.IDENTIFIER().getText()
        self.visit(ctx.expression())
        if var_name not in self.symbol_table:
            raise Exception(f"Undefined variable: {var_name}")
        var_type = self.symbol_table[var_name][1]
        self.bytecode.append(('STORE', self.symbol_table[var_name][0], var_type))

    def visitIfStmt(self, ctx):
        end_label = self.new_label()
        else_label = self.new_label()
        self.visit(ctx.expression())
        self.bytecode.append(('JMP_IF_FALSE', else_label))
        self.visit(ctx.block(0))
        self.bytecode.append(('JMP', end_label))
        self.bytecode.append(('LABEL', else_label))
        if ctx.block(1):
            self.visit(ctx.block(1))
        self.bytecode.append(('LABEL', end_label))

    def visitWhileStmt(self, ctx):
        start_label = self.new_label()
        end_label = self.new_label()
        self.bytecode.append(('LABEL', start_label))
        self.visit(ctx.expression())
        self.bytecode.append(('JMP_IF_FALSE', end_label))
        self.visit(ctx.block())
        self.bytecode.append(('JMP', start_label))
        self.bytecode.append(('LABEL', end_label))

    def visitFuncDefStmt(self, ctx):
        func_name = ctx.IDENTIFIER().getText()
        param_list = [(p.TYPE().getText(), p.IDENTIFIER().getText()) for p in ctx.parameters().param()] if ctx.parameters() else []
        old_symbol_table = self.symbol_table
        self.symbol_table = old_symbol_table.copy()
        self.next_var_address = max(addr for addr, _ in self.symbol_table.values()) + 1 if self.symbol_table else 0
        self.bytecode.append(('FUNC_DEF', func_name, str(len(param_list))))
        for i, (param_type, param_name) in enumerate(param_list):
            self.symbol_table[param_name] = (self.next_var_address, param_type)
            self.bytecode.append(('STORE', str(self.next_var_address), param_type))
            self.next_var_address += 1
        self.current_function = func_name
        self.functions[func_name] = (param_list, self.symbol_table.copy())
        self.visit(ctx.block())
        self.visit(ctx.expression())
        self.bytecode.append(('RETURN',))
        self.symbol_table = old_symbol_table
        self.current_function = None

    def visitFunctionCallExpr(self, ctx):
        func_name = ctx.IDENTIFIER().getText()
        args = ctx.arguments().expression() if ctx.arguments() else []
        for arg in reversed(args):
            self.visit(arg)
        self.bytecode.append(('CALL', func_name, len(args)))

    def visitNumberExpr(self, ctx):
        value = ctx.NUMBER().getText()
        if '.' in value:
            self.bytecode.append(('PUSH', float(value)))
        else:
            self.bytecode.append(('PUSH', int(value)))

    def visitBoolExpr(self, ctx):
        value = ctx.BOOL().getText().lower() == 'true'
        self.bytecode.append(('PUSH', value))

    def visitVariableExpr(self, ctx):
        var_name = ctx.IDENTIFIER().getText()
        if var_name not in self.symbol_table:
            raise Exception(f"Undefined variable: {var_name}")
        self.bytecode.append(('LOAD', self.symbol_table[var_name][0]))

    def visitParenExpr(self, ctx):
        return self.visit(ctx.expression())

    def visitMulDivExpr(self, ctx):
        self.visit(ctx.expression(0))
        self.visit(ctx.expression(1))
        op = ctx.op.text
        self.bytecode.append(('MUL' if op == '*' else 'DIV',))

    def check_types(self, left_type, right_type, operation):
        if left_type != right_type:
            raise Exception(f"Type mismatch: Cannot perform {operation} on {left_type} and {right_type}")

    def visitAddSubExpr(self, ctx):
        left_type = self.visit(ctx.expression(0))
        right_type = self.visit(ctx.expression(1))
        self.check_types(left_type, right_type, ctx.op.text)
        op = ctx.op.text
        self.bytecode.append(('ADD' if op == '+' else 'SUB',))
        return left_type

    def visitComparisonExpr(self, ctx):
        self.visit(ctx.expression(0))
        self.visit(ctx.expression(1))
        op = ctx.op.text
        self.bytecode.append(('CMP', op))

    def compile(self, tree):
        self.visit(tree)
        return self.bytecode, self.symbol_table, self.functions

def main():
    if len(sys.argv) < 3:
        print("Usage: python compiler.py <input_file> <output_file>")
        return

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    try:
        with open(input_file, 'r') as file:
            input_string = file.read()

        lexer = ExpressionLexer(InputStream(input_string))
        stream = CommonTokenStream(lexer)
        parser = ExpressionParser(stream)
        tree = parser.program()

        compiler = Compiler()
        bytecode, symbol_table, functions = compiler.compile(tree)

        with open(output_file, 'w') as file:
    
            file.write("BYTECODE\n")
            for instr in bytecode:
                file.write(','.join(map(str, instr)) + '\n')
            
            file.write("SYMBOL_TABLE\n")
            for var, (addr, type_) in symbol_table.items():
                file.write(f"{var},{addr},{type_}\n")
            
            file.write("FUNCTIONS\n")
            for func, (params, func_symbol_table) in functions.items():
                file.write(f"{func}:{','.join(f'{p[0]} {p[1]}' for p in params)}\n")
                for var, (addr, type_) in func_symbol_table.items():
                    file.write(f"  {var},{addr},{type_}\n")

        print(f"Compilation successful. Bytecode written to {output_file}")

    except Exception as e:
        print(f"Compilation error: {e}")

if __name__ == '__main__':
    main()
