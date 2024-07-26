import sys

class StackFrame:
    def __init__(self, return_address, local_memory, local_symbol_table):
        self.return_address = return_address
        self.local_memory = local_memory
        self.local_symbol_table = local_symbol_table

class StackVM:
    def __init__(self):
        self.stack = []
        self.memory = [] * 10  # Initialize memory with 10 slots
        self.pc = 0
        self.functions = {}
        self.frames = []
        self.output = []
        self.return_value = None
        self.bytecode = []
        self.global_symbol_table = {}

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
        self.global_symbol_table = symbol_table
        print("Debug: Starting execution")

        while self.pc < len(self.bytecode):
            instruction = self.bytecode[self.pc]
            op = instruction[0]
            print(f"Debug: Executing instruction {self.pc}: {instruction}")
            
            try:
                if op == 'PUSH':
                    value = instruction[1]
                    if value == 'None':
                        value = 'None'
                    else:
                        try:
                            value = int(value)
                        except ValueError:
                            try:
                                value = float(value)
                            except ValueError:
                                pass
                        self.push(value)
                elif op == 'LOAD':
                    address = int(instruction[1])
                    self.ensure_memory_size(address)
                    value = self.memory[address]
                    if value is None:
                        raise Exception(f"Attempting to load uninitialized value from address {address}")
                    self.push(value)
                    print(f"Debug: Loaded {value} from address {address}")
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
                    #self.push(value)
                    self.memory[address] = value
                    print(f"Debug: Stored {value} at address {address}")
                elif op == 'CREATE_ARRAY':
                    size = int(instruction[1])
                    self.push([])
                elif op == 'ARRAY_PUSH':
                    value = self.pop()
                    array = self.pop()
                    array.append(value)
                    self.push(array)
                elif op == 'ARRAY_POP':
                    array = self.pop()
                    if not isinstance(array, list):
                        raise Exception("Array pop operation on non-array object")
                    if len(array) == 0:
                        raise Exception("Cannot pop from an empty array")
                    array.pop()
                    self.push(array)
                elif op == 'STORE_ARRAY':
                    array = self.pop()
                    address = int(instruction[1])
                    var_type = instruction[2]
                    self.ensure_memory_size(address)
                    if not isinstance(array, list):
                        raise Exception(f"Cannot store non-array value in array variable")
                    self.memory[address] = array
                elif op == 'LOAD_ARRAY':
                    address = int(instruction[1])
                    self.ensure_memory_size(address)
                    array = self.memory[address]
                    if not isinstance(array, list):
                        raise Exception(f"Attempting to load non-array value as array from address {address}")
                    self.push(array)
                elif op == 'ARRAY_LOAD':
                    index = self.pop()
                    array = self.pop()
                    if not isinstance(array, list):
                        raise Exception("Array load operation on non-array object")
                    if index < 0 or index >= len(array):
                        raise Exception("Array index out of bounds")
                    self.push(array[index])
                elif op == 'PRINT':
                    value = self.pop()
                    self.output.append(str(value))
                    print(f"Debug: Printing value: {value}")
                elif op == 'ADD':
                    b, a = self.pop(), self.pop()
                    if isinstance(a, str) and isinstance(b, str):
                        a = a[1:-1]
                        b = b[1:-1]
                        result = str(b) + str(a)
                        self.push(result)
                    elif (isinstance(a, int) or isinstance(a, float)) and (isinstance(b, int) or isinstance(b, float)):
                        result = a + b
                        self.push(result)
                    elif (isinstance(a,int) and isinstance(b,str)) or (isinstance(a,int) and isinstance(b,str)):
                        raise Exception("String and int can't be added")
                elif op in ['SUB', 'MUL', 'DIV']:
                    b, a = self.pop(), self.pop()
                    if op == 'SUB':
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
                    func_pc = self.pc + 1
                    func_end = self.find_func_end(self.pc)
                    self.functions[func_name] = (func_pc, num_params, func_end)
                    self.pc = func_end + 1
                    continue
                elif op == 'CALL':
                    func_name = instruction[1]
                    num_args = int(instruction[2])
                    self.call_function(func_name, num_args)
                    continue
                elif op == 'RETURN':
                    if self.frames:
                        self.return_from_function()
                    else:
                        break
                    continue
                self.pc += 1
                print(f"Stack state: {self.stack}")
            except Exception as e:
                print(f"Error at PC {self.pc}, Instruction: {instruction}")
                print(f"Stack state: {self.stack}")
                print(f"Memory state: {self.memory}")
                raise Exception(f"Runtime error at instruction {self.pc}: {instruction}\n{str(e)}")

    def call_function(self, func_name, num_args):
        if func_name not in self.functions:
            raise Exception(f"Undefined function: {func_name}")
        func_start, param_count, func_end = self.functions[func_name]
        if num_args != param_count:
            raise Exception(f"Function {func_name} expects {param_count} arguments, but got {num_args}")
        new_frame = StackFrame(self.pc + 1, self.memory.copy(), self.global_symbol_table.copy())
        self.frames.append(new_frame)
        # Extend the memory to accommodate local variables
        self.memory.extend([None] * param_count)
        self.pc = func_start
    
    def return_from_function(self):
        if not self.frames:
            raise Exception("Cannot return from top-level code")
        return_value = self.pop() if self.stack else None
        frame = self.frames.pop()
        self.pc = frame.return_address
        # Preserve changes to global variables
        for var, (addr, _) in self.global_symbol_table.items():
            if addr < len(frame.local_memory):
                self.memory[addr] = frame.local_memory[addr]
        if return_value is not None:
            self.push(return_value)

    def load_variable(self, var_name):
        if var_name in self.global_symbol_table:
            address, _ = self.global_symbol_table[var_name]
            self.ensure_memory_size(address)
            value = self.memory[address]
            if value is None:
                raise Exception(f"Attempting to load uninitialized variable: {var_name}")
            return value
        raise Exception(f"Undefined variable: {var_name}")

    def store_variable(self, var_name, value, var_type):
        if var_name in self.global_symbol_table:
            address, _ = self.global_symbol_table[var_name]
        else:
            address = len(self.memory)
            self.global_symbol_table[var_name] = (address, var_type)
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
    
    def find_func_end(self, start):
        depth = 0
        for i in range(start, len(self.bytecode)):
            if self.bytecode[i][0] == 'FUNC_DEF':
                depth += 1
            elif self.bytecode[i][0] == 'RETURN':
                depth -= 1
                if depth == 0:
                    return i
        raise Exception("Function end not found")
    
    def find_label(self, label):
        for i, instr in enumerate(self.bytecode):
            if instr[0] == 'LABEL' and instr[1] == label:
                return i
        raise Exception(f"Label not found: {label}")
    
    def create_array(self, size):
        return [None] * size

    def array_store(self):
        value = self.pop()
        index = self.pop()
        array = self.pop()
        if not isinstance(array, list):
            raise Exception("Array store operation on non-array object")
        if index < 0 or index >= len(array):
            raise Exception("Array index out of bounds")
        array[index] = value

    def array_load(self):
        index = self.pop()
        array = self.pop()
        if not isinstance(array, list):
            raise Exception("Array load operation on non-array object")
        if index < 0 or index >= len(array):
            raise Exception("Array index out of bounds")
        self.push(array[index])

    def array_length(self):
        array = self.pop()
        if not isinstance(array, list):
            raise Exception("Array length operation on non-array object")
        self.push(len(array))
            
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
