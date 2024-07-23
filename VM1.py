import sys
class StackVM:
    def __init__(self):
        self.stack = []
        self.memory = [None] * 10  # Initialize memory with 1000 slots
        self.pc = 0
        self.functions = {}
        self.call_stack = []
        self.output = []
        self.return_value = None
        self.bytecode = []

    def ensure_memory_size(self, address):
        if address >= len(self.memory):
            self.memory.extend([None] * (address - len(self.memory) + 1))

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
        self.functions = functions
        print("Debug: Starting execution")
        print(f"Debug: Bytecode: {self.bytecode}")

        while self.pc < len(self.bytecode):
            instruction = self.bytecode[self.pc]
            op = instruction[0]
            print(f"Debug: Executing instruction {self.pc}: {instruction}")
            try:
                if op == 'PUSH':
                    value = instruction[1]
                    try:
                        value = int(value)
                    except ValueError:
                        try:
                            value = float(value)
                        except ValueError:
                           pass
                    self.stack.append(value)
                elif op == 'LOAD':
                    address = int(instruction[1])
                    self.ensure_memory_size(address)
                    self.push(self.memory[address])
                    print(f"Debug: Loaded {self.memory[address]} from address {address}")
                elif op == 'STORE':
                    value = self.pop()
                    address, var_type = int(instruction[1]), instruction[2]
                    self.ensure_memory_size(address)
                    if var_type == 'int':
                        value = int(value)
                    elif var_type == 'float':
                        value = float(value)
                    elif var_type == 'bool':
                        value = bool(value)
                    elif var_type == 'string':
                        value = str(value)
                    self.memory[address] = value
                    print(f"Debug: Stored {value} at address {address}")
                elif op == 'PRINT':
                    value = self.pop()
                    self.output.append(str(value))
                    print(f"Debug: Printing value: {value}")
                elif op == 'ADD':
                    b, a = self.pop(), self.pop()
                    if isinstance(a, str) or isinstance(b, str):
                        result = str(a) + str(b)
                    else:
                        result = a + b
                    self.push(result)
                    print(f"Debug: Added {a} and {b}, pushed result {result}")
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
                elif op == 'INC':
                    address = int(instruction[1])
                    value = self.memory[address]
                    if isinstance(value, str):
                        value = int(value)
                    self.memory[address] = value + 1
                elif op == 'DEC':
                    address = int(instruction[1])
                    value = self.memory[address]
                    if isinstance(value, str):
                        value = int(value)
                    self.memory[address] = value - 1
                elif op == 'CMP':
                    b, a = self.pop(), self.pop()
                    cmp_op = instruction[1]
                    try:
                        if isinstance(a, str) and a.isdigit():
                            a = int(a)
                        if isinstance(b, str) and b.isdigit():
                            b = int(b)
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
                    except TypeError:
                        raise Exception(f"Cannot compare {type(a)} and {type(b)} using {cmp_op}")
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
                        self.call_stack.append((self.pc + 1, self.memory.copy()))
                        func_pc, param_count = self.functions[func_name]
                        new_memory = [None] * param_count
                        for i in range(num_args - 1, -1, -1):
                            new_memory[i] = self.pop()
                        self.memory = new_memory
                        self.pc = func_pc
                        continue
                elif op == 'RETURN':
                        if self.call_stack:
                            self.return_value = self.pop() 
                            self.pc, self.memory = self.call_stack.pop()
                            self.push(self.return_value)
                            continue
                        else:
                            self.return_value = self.pop()
                self.pc += 1
            except Exception as e:
                print(f"Error at PC {self.pc}, Instruction: {instruction}")
                print(f"Stack state: {self.stack}")
                print(f"Memory state: {self.memory}")
                raise Exception(f"Runtime error at instruction {self.pc}: {instruction}\n{str(e)}")

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
                lines = file.readlines()
                if not lines:
                    raise ValueError("Empty bytecode file")

                for line in lines:
                    line = line.strip()
                    if not line:
                        continue
                    elif line == "BYTECODE":
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

            if not bytecode:
                raise ValueError("No bytecode instructions found in file")
            return bytecode, symbol_table, functions

def main():
    if len(sys.argv) < 2:
        print("Usage: python vm.py <bytecode_file>")
        return
    bytecode_file = sys.argv[1]
    try:
        bytecode, symbol_table, functions = StackVM.parse_bytecode_file(bytecode_file)

        vm = StackVM()
        vm.run(bytecode, symbol_table, functions)

        print("\nProgram Output:")
        for line in vm.get_output():
            print(line)
        
        print("\nSymbol table: ")
        for var, (address, var_type) in symbol_table.items():
            value = vm.memory[address] if address < len(vm.memory) else None
            print(f"{var} ({var_type}): {value}")

    except Exception as e:
        print(f"Runtime error: {e}")

if __name__ == '__main__':
    main()
