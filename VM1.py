import sys
class StackVM:
    def __init__(self):
        self.stack = []
        self.memory = []
        self.pc = 0
        self.functions = {}
        self.call_stack = []
        self.output = []
        self.return_value = None  # Store return value if needed

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if not self.stack:
            raise Exception("Stack underflow: Attempted to pop from an empty stack")
        return self.stack.pop()

    def peek(self):
        if not self.stack:
            raise Exception("Stack underflow: Attempted to peek an empty stack")
        return self.stack[-1]

    def run(self, bytecode, symbol_table, functions):
        self.bytecode = bytecode
        self.global_symbol_table = symbol_table
        self.functions = functions
        self.memory = [None] * (max(addr for addr, _ in symbol_table.values()) + 1)
        
        while self.pc < len(self.bytecode):
            instruction = self.bytecode[self.pc]
            op = instruction[0]
            try:
                if op == 'PUSH':
                    self.push(instruction[1])
                elif op == 'LOAD':
                    address = int(instruction[1])
                    self.push(self.memory[address])
                elif op == 'STORE':
                    value = self.pop()
                    address, var_type = int(instruction[1]), instruction[2]
                    if var_type == 'int':
                        value = int(value)
                    elif var_type == 'float':
                        value = float(value)
                    elif var_type == 'bool':
                        value = bool(value)
                    self.memory[address] = value
                elif op == 'PRINT':
                    value = self.pop()
                    self.output.append(str(value))  # Append to output
                    print(f"Outputting: {value}")  # Debug print statement
                elif op in ['ADD', 'SUB', 'MUL', 'DIV']:
                    b, a = self.pop(), self.pop()
                    if op == 'ADD':
                        self.push(a + b)
                    elif op == 'SUB':
                        self.push(a - b)
                    elif op == 'MUL':
                        self.push(a * b)
                    elif op == 'DIV':
                        self.push(a / b if isinstance(a, float) or isinstance(b, float) else a // b)
                elif op == 'CMP':
                    b, a = self.pop(), self.pop()
                    cmp_op = instruction[1]
                    if cmp_op == '==':
                        self.push(a == b)
                    elif cmp_op == '!=':
                        self.push(a != b)
                    elif cmp_op == '<':
                        self.push(a < b)
                    elif cmp_op == '>':
                        self.push(a > b)
                    elif cmp_op == '<=':
                        self.push(a <= b)
                    elif cmp_op == '>=':
                        self.push(a >= b)
                elif op == 'JMP':
                    self.pc = self.find_label(instruction[1])
                    continue
                elif op == 'JMP_IF_FALSE':
                    cond = self.pop()
                    if not cond:
                        self.pc = self.find_label(instruction[1])
                        continue
                elif op == 'LABEL':
                    pass  # Labels are resolved during compilation
                elif op == 'FUNC_DEF':
                    func_name = instruction[1]
                    num_params = int(instruction[2])
                    self.functions[func_name] = (self.pc + 1, num_params)
                elif op == 'CALL':
                    func_name = instruction[1]
                    num_args = int(instruction[2])
                    if func_name not in self.functions:
                        raise Exception(f"Undefined function: {func_name}")
                    
                    # Save current state
                    self.call_stack.append((self.pc + 1, self.memory.copy()))
                    
                    # Set up new memory frame for function
                    func_pc, param_count = self.functions[func_name]
                    new_memory = [None] * param_count
                    
                    # Pass arguments
                    for i in range(num_args - 1, -1, -1):
                        new_memory[i] = self.pop()
                    
                    self.memory = new_memory
                    self.pc = func_pc
                    continue
                elif op == 'RETURN':
                    if self.call_stack:
                        self.return_value = self.pop()  # Store return value
                        
                        # Restore previous state
                        self.pc, self.memory = self.call_stack.pop()
                        
                        # Push return value to the stack for further use
                        self.push(self.return_value)
                        continue
                    else:
                        # No function to return from, continue to end
                        self.return_value = self.pop()
                
                self.pc += 1
            except Exception as e:
                raise Exception(f"Runtime error at instruction {self.pc}: {instruction}\n{str(e)}")
        
        # After the bytecode is done executing
        print("End of bytecode reached.")
        return self.return_value

    def find_label(self, label):
        for i, instr in enumerate(self.bytecode):
            if instr[0] == 'LABEL' and instr[1] == label:
                return i
        raise Exception(f"Label not found: {label}")
    
    def get_output(self):
        return self.output

    @staticmethod
    def parse_bytecode_file(filename):
        bytecode = []
        symbol_table = {}
        functions = {}
        current_section = None
        current_function = None

        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                
                if line == "BYTECODE":
                    current_section = "bytecode"
                elif line == "SYMBOL_TABLE":
                    current_section = "symbol_table"
                elif line == "FUNCTIONS":
                    current_section = "functions"
                elif current_section == "bytecode":
                    bytecode.append(tuple(line.split(',')))
                elif current_section == "symbol_table":
                    var, addr, type_ = line.split(',')
                    symbol_table[var] = (int(addr), type_)
                elif current_section == "functions":
                    if ':' in line:
                        func_name, params_str = line.split(':')
                        params = [tuple(p.split()) for p in params_str.split(',') if p]
                        functions[func_name] = (params, {})
                        current_function = func_name
                    else:
                        var, addr, type_ = line.strip().split(',')
                        functions[current_function][1][var] = (int(addr), type_)

        return bytecode, symbol_table, functions

def main():
    if len(sys.argv) < 2:
        print("Usage: python vm.py <bytecode_file>")
        return

    bytecode_file = sys.argv[1]

    try:
        bytecode, symbol_table, functions = StackVM.parse_bytecode_file(bytecode_file)

        vm = StackVM()
        result = vm.run(bytecode, symbol_table, functions)

        print("Program Output:")
        for line in vm.get_output():
            print(line)

        if result is not None:
            print(f"{result}")

        print("\nSymbol table: ")
        for var, (address, var_type) in symbol_table.items():
            value = vm.memory[address]
            print(f"{var} ({var_type}): {value}")

    except Exception as e:
        print(f"Runtime error: {e}")

if __name__ == '__main__':
    main()
