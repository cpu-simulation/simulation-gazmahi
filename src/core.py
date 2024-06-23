from pprint import pprint
from compiler import compiler


class Register:
    def __init__(self, size):
        self.size = size
        self.value = 0

    def read(self):
        return self.value

    def write(self, value):
        self.value = value & ((1 << self.size) - 1)


class Memory:
    def __init__(self, size=4096):
        self.size = size
        self.memory = [0] * size

    def read(self, address):
        return self.memory[address]

    def write(self, address, value):
        self.memory[address] = value


class ALU:
    def add(self, a, b):
        result = a + b
        carry = result > 0xFFFF
        return result & 0xFFFF, carry

    def sub(self, a, b):
        result = a - b
        carry = result < 0
        return result & 0xFFFF, carry



class Register:
    def __init__(self, size):
        self.size = size
        self.value = 0

    def read(self):
        return self.value

    def write(self, value):
        self.value = value & ((1 << self.size) - 1)


class Memory:
    def __init__(self, size=4096):
        self.size = size
        self.memory = [0] * size

    def read(self, address):
        return self.memory[address]

    def write(self, address, value):
        self.memory[address] = value


class ALU:
    def add(self, a, b):
        result = a + b
        carry = result > 0xFFFF
        return result & 0xFFFF, carry

    def sub(self, a, b):
        result = a - b
        carry = result < 0
        return result & 0xFFFF, carry


class Core:
    def __init__(self) -> None:
        self.memory = []
        self.registers = [{"AC": "0X0000"}, {"IR": "0X0000"}, {"AR": "0X000"}, {"DR": "0X0000"}, {"INPR": "0X00"}, {"PC": "0X000"}, {"OUTR": "0X00"}, {"TR": "0X0000"}, {"E": "0"}]


    def memory_write(self, data: dict) -> None:
        if data not in self.memory:
            self.memory.append(data)

    
    def memory_bulk_write(self, data: list[dict]) -> None:
        for item in data:
            if item not in self.memory:
                self.memory.append(item)        
    
    
    def memory_bulk_read(self) -> list[dict]:
        print("-" * 40)
        for item in self.memory:
            print(f"address {self.memory.index(item)}:  {list(item.keys())[0]}\nvalue: {list(item.values())[0]}")
        print("-" * 40)
        
    
    
    def memory_read(self, address) -> dict:
        for item in self.memory:
            if item.get(address):
                return  f"address:  {list(item.keys())[0]}\nvalue: {list(item.values())[0]}" 

  
        
    def register_write(self, data: dict[int, int]) -> None:
        for key in data.keys():
            for reg in self.registers:
                if reg.get(key) == 0:
                    reg[key] = data[key]


    
    
    def register_read(self) -> dict[int, int]: 
        print("-" * 40)
        print(f"Registers: {self.registers}")
        print("-" * 40)




    @staticmethod
    def compiling_instructions(instructions: list[str]) -> list[str]:
        return compiler()


              

    def save_in_memorry(self, machinecode: list[str]) -> None:
        """save the machine codes in the memory cells of the object(a.k. self.memory)

        Args:
            machinecode (list[str]): the list of machine codes instructions
        """
        ar = 0
        for code in machinecode:
            self.memory_write({hex(ar): code})
            ar += 1 
        self.memory_bulk_read()



    
    def compile(self, instructions: list[str]) -> None:
        machine_code_instrucions =  self.compiling_instructions(instructions)
        self.save_in_memorry(machine_code_instrucions)



    def execute(self):
        # self.memory = Memory()
        self.accumulator = Register(16)
        self.pc = Register(12)  # Program Counter
        self.carry = False
        self.zero = False
        while True:
            instruction = self.memory.read(self.pc.read())
            opcode = (instruction & 0xF000) >> 12
            operand = instruction & 0x0FFF

            if opcode == 0x0:  # HLT
                break
            elif opcode == 0x1:  # LDA
                self.lda(operand)
            elif opcode == 0x2:  # STA
                self.sta(operand)
            elif opcode == 0x3:  # ADD
                self.add(operand)
            elif opcode == 0x4:  # SUB
                self.sub(operand)
            elif opcode == 0x5:  # IN
                self._in(operand)
            elif opcode == 0x6:  # OUT
                self.out(operand)
            elif opcode == 0x7:  # JMP
                self.jmp(operand)
            elif opcode == 0x8:  # JZ
                self.jz(operand)
            elif opcode == 0x9:  # JC
                self.jc(operand)
            else:
                raise ValueError(f"Invalid opcode {opcode}")

            self.pc.write(self.pc.read() + 1)

    def lda(self, address):
        value = self.memory.read(address)
        self.accumulator.write(value)
        self.update_flags(value)

    def sta(self, address):
        value = self.accumulator.read()
        self.memory.write(address, value)

    def add(self, address):
        value = self.memory.read(address)
        result = self.accumulator.read() + value
        self.accumulator.write(result & 0xFFFF)
        self.carry = result > 0xFFFF
        self.update_flags(result)

    def sub(self, address):
        value = self.memory.read(address)
        result = self.accumulator.read() - value
        self.accumulator.write(result & 0xFFFF)
        self.carry = result < 0
        self.update_flags(result)

    def _in(self, address):
        # For simplicity, assume input is provided externally
        value = external_input()
        self.memory.write(address, value)

    def out(self, address):
        value = self.memory.read(address)
        external_output(value)

    def jmp(self, address):
        self.pc.write(address)

    def jz(self, address):
        if self.zero:
            self.pc.write(address)

    def jc(self, address):
        if self.carry:
            self.pc.write(address)

    def update_flags(self, value):
        self.zero = (value == 0)
        self.carry = (value > 0xFFFF)

# Example external input/output functions
def external_input():
    # Placeholder for actual input handling
    return 0x1234

def external_output(value):
    # Placeholder for actual output handling
    print(f"Output: {value:04X}")

                    
    




def main():
    c = Core()
    c.memory_bulk_write([{"0XFE": "0X12"}, {"0XFF": "0X13"}])
    c.memory_bulk_read()
    c.compile(["0 ADD 74f", "1 BSA 54C", "0 ISZ 001", "CLA", "HLT", "INC", "SZA"])
    print(c.memory)

    



if __name__ == "__main__":
    main()