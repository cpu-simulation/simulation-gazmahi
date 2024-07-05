from compiler import compiler


class Register:
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.value = 0X0

    def read(self):
        return self.value

    def write(self, value):
        self.value = value

    def info(self):
        print(f"name: {self.name}, size: {self.size}, value: {self.value}")
    


class Memory:
    def __init__(self, size=4096):
        self.size = size
        self.memory = [0] * size
        self.active_addresses = []

    def read(self, address):
        return self.memory[address]

    def write(self, address, value):
        self.active_addresses.append(address)
        self.memory[address] = value

    def bulk_read(self):
        for add in self.active_addresses:
            print("-"*40)
            print(f"add: {add}, value: {self.read(add)}")
            print("-"*40)



class ALU:
    def Add(self, a, b):
        if isinstance(a, str):
            a = int(a, 16)
        if isinstance(b, str):
            b = int(b, 16)
        result = a + b
        carry = result > 0xFFFF
        return result & 0xFFFF, carry

    def Sub(self, a, b):
        result = a - b
        carry = result < 0
        return result & 0xFFFF, carry


    def And(self, a, b):
        if isinstance(a, str):
            a = int(a, 16)
        if isinstance(b, str):
            b = int(b, 16)
        result = a & b
        return hex(result)
    
    def Rshift(self, a, n):
        if isinstance(a, str):
            a = int(a, 16)
        result = a >> n
        return hex(result)


    def Lshift(self, a, n):
        if isinstance(a, str):
            a = int(a, 16)
        result = a << n
        return hex(result)
    
    def inverse(self, a):
        if isinstance(a, str):
            a = int(a, 16)
        result = ~a
        return hex(result)
    

    def Or(self, a, b):
        if isinstance(a, str):
            a = int(a, 16)
        if isinstance(b, str):
            b = int(b, 16)
        result = a | b
        return hex(result)

    def Inc(self, a):
        if isinstance(a, str):
            a = int(a, 16)    
        result = (a + 1) &  0xFFFF
        return hex(result)
    
    def equal(self, a, b):
        if isinstance(a, str):
            a = int(a, 16)
        if isinstance(b, str):
            b = int(b, 16)
        result = (a == b)
        return result
    

    def greater_equal_than(self, a, b):
        if isinstance(a, str):
            a = int(a, 16)
        if isinstance(b, str):
            b = int(b, 16)
        result = (a >= b)
        return result

    def less_equal_than(self, a, b):
        if isinstance(a, str):
            a = int(a, 16)
        if isinstance(b, str):
            b = int(b, 16)
        result = (a >= b)
        return result

    def greater_than(self, a, b):
        if isinstance(a, str):
            a = int(a, 16)
        if isinstance(b, str):
            b = int(b, 16)
        result = (a > b)
        return result
    
    def less_than(self, a, b):
        if isinstance(a, str):
            a = int(a, 16)
        if isinstance(b, str):
            b = int(b, 16)
        result = (a < b)
        return result
    


class Core:
    def __init__(self) -> None:
        self.memory = Memory()
        self.registers = [] # container for registers objects
        # making objects and adding them to the self.registers
        for i,j in [("AC",16),("IR",16),("AR",16),("DR",16),("INPR",16),("PC",16),("OUTR",16),("TR",16),("E",1)]:
            reg = Register(i, j)
            self.registers.append(reg)
        self.ALU = ALU()


    def memory_write(self, data: dict[str: int]) -> None:
        for key, value in data.items():
            self.memory.write(key, value)


    def memory_bulk_write(self, data: list[dict]) -> None:
        for cell in data:
            self.memory_write(cell)
    
    
    def memory_bulk_read(self) -> list[dict]:
        self.memory.bulk_read()
        
    
    
    def memory_read(self, address: int) -> dict:
        if 0 <= address <= 4095:
            return self.memory.read(address)
        else:
            raise ValueError(f"invalid address cell")

  
        
    def register_write(self, data: dict[int, int]) -> None:
        for label, value in data.items():
            for reg in self.registers:
                if reg.name == label:
                    reg.write(value)
                    break
            else:
                raise ValueError(f"there is no register with {label} name")

    
    
    def register_read(self, reg_name: str) -> int: 
        for reg in self.registers:
            if reg.name == reg_name:
                return reg.read()
        else:
            raise ValueError(f"there is not a register named: {reg_name}")


    def registers_info(self):
        print("-" * 40)
        for reg in self.registers:
            reg.info()      
        print("-" * 40)


    @staticmethod
    def compiling_instructions(instructions: list[str]) -> list[str]:
        return compiler(instructions)



    def save_in_memorry(self, machinecode: list[str]) -> None:
        """save the machine codes in the memory cells of the object(a.k. self.memory)

        Args:
            machinecode (list[str]): the list of machine codes instructions
        """
        ar = 0
        for code in machinecode:
            self.memory.write(ar, code)
            ar += 1

 
    def compile(self, instructions: list[str]) -> None:
        self.machine_code_instrucions =  self.compiling_instructions(instructions)
        self.save_in_memorry(self.machine_code_instrucions)



    def fetch_and_decode(self):
        self.PC = self.register_read("PC")
        self.register_write({"AR": self.PC})
        print(self.machine_code_instrucions)
        
        self.carry = False
        self.zero = False
        # while True:
        for instruct in self.machine_code_instrucions:
            # retrieving address register through PC number
            IR = self.memory.read(self.PC) # EX: "0X4001"
            self.PC += 1
            self.register_write({"PC": self.PC})

            
            opcode = (self.ALU.And(IR, 0XF000)) # EX: "0x4000"
            opcode = self.ALU.Rshift(opcode , 12) # EX: "0X4"
            operand = self.ALU.And(IR, 0X0FFF) # EX: "0X1" or "0X800"
            print(opcode, operand)

            if opcode == "0x7":
                self.register_based_instruction(operand)
            else:
                self.memory_based_instruction(opcode, operand)


    def register_based_instruction(self, operand):
        def CLA():
            self.register_write({"AC": 0})
            self.registers_info()

        def CLE():
            self.register_write({"E": 0})
            self.registers_info()

        def CMA():
            AC = self.register_read("AC")
            AC = self.ALU.inverse(AC) # ~AC
            self.register_write({"AC": self.ALU.And(AC, 0xFFFf)}) # AC & 0xFFFF
            self.registers_info()


        def CME():
            E = self.register_read("E")
            E = self.ALU.inverse(E) # ~E
            self.register_write({"E": self.ALU.And(E, 0x1)}) # E & 0x1
            self.registers_info()


        def CIR():
            AC = self.register_read("AC")
            E = self.register_read("E")
            new_E = self.ALU.And(AC, 0x1) # AC & 0x1
            AC = self.ALU.Or(self.ALU.Rshift(AC, 1), self.ALU.Lshift(E, 15)) #(AC >> 1) | (E << 15)  
            self.register_write({"AC": AC})
            self.register_write({"E": new_E})
            self.registers_info()


        def CIL(): 
            AC = self.register_read("AC")
            E = self.register_read("E")
            new_E = self.ALU.And(self.ALU.Rshift(AC, 15), 0x1) # (AC >> 15) & 0x1  
            AC = self.ALU.Or(self.ALU.And(self.ALU.Lshift(AC, 1), 0xFFFF), E)# ((AC << 1) & 0xFFFF) | E  
            self.register_write({"AC": AC})
            self.register_write({"E": new_E})
            self.registers_info()


        def INC(): 
            AC = self.register_read("AC")
            AC = self.ALU.Inc(AC) #(AC + 1) & 0xFFFF
            self.register_write({"AC": AC})  
            self.registers_info()


        def SPA():
            AC = self.register_read("AC")
            if self.ALU.greater_equal_than(AC, 0): # AC >= 0
                self.PC = self.register_read("PC")
                self.PC += 1
                self.register_write({"PC": self.PC}) 
            self.registers_info()

        def SNA():
            AC = self.register_read("AC")
            if self.ALU.less_than(AC, 0): # AC < 0
                self.PC = self.register_read("PC")
                self.PC += 1
                self.register_write({"PC": self.PC})  
            self.registers_info()

                    
        def SZA():
            AC = self.register_read("AC")
            if self.ALU.equal(AC, 0): # AC == 0
                self.PC = self.register_read("PC")
                self.PC += 1
                self.register_write({"PC": self.PC})
            self.registers_info()


        def SZE():
            E = self.register_read("E")
            if self.ALU.equal(E, 0): # E == 0
                self.PC = self.register_read("PC")
                self.PC += 1
                self.register_write({"PC": self.PC})
            self.registers_info()



        def HLT(): 
            raise SystemExit("HALT instruction executed. Stopping the CPU.")         



        
        print("register based")
        if operand == "0x800":
            print("CLA")
            CLA()
        elif operand == "0x400":
            print("CLA")
            CLE()
        elif operand == "0x200":
            print("CMA")
            CMA()
        elif operand == "0x100":
            print("CME")
            CME()
        elif operand == "0x80":
            print("CIR")
            CIR()
        elif operand == "0x40":
            print("CIL")
            CIL()
        elif operand == "0x20":
            print("INC")
            INC()
        elif operand == "0x10":
            print("SPA")
            SPA()
        elif operand == "0x8":
            print("SNA")
            SNA()
        elif operand == "0x4":
            print("SZA")
            SZA()
        elif operand == "0x2":
            print("SZE")
            SZE()
        elif operand == "0x1":
            print("HLT")
            HLT()
            


    def memory_based_instruction(self, opcode, operand):
        def AND(opcode, operand):
            ...
            # if opcode == 0X0:
            #     pass
            # else:
            #     operand = self.memory_read(operand)
            
            # self.register_write({"DR": operand})
            # DR = self.register_read("DR")
            # AC = self.register_read("AC")
            # self.register_write({"AC": AC & DR})    

        
        def ADD(opcode, operand):
            ...
            # if opcode == 0X1:
            #     pass
            # else:
            #     operand = self.memory_read(operand)

            # self.register_write({"DR": operand})
            # DR = self.register_read("DR")
            # AC = self.register_read("AC")
            # result, carry = self.ALU.add(AC, DR)
            # self.register_write({"AC": result})
            # self.register_write({"E": carry})
            
        def LDA(opcode, operand):
            ...
            # if opcode == 0X2:
            #     pass
            # else:
            #     operand = self.memory_read(operand)
            
            # self.register_write({"DR": operand})
            # DR = self.register_read("DR")
            # self.register_write({"AC": DR})    



        def STA(opcode, operand):
            ...
            # if opcode == 0X3:
            #     pass
            # else:
            #     operand = self.memory_read(operand)
            

            # AC = self.register_read("AC")
            # self.memory_write({operand: AC})


        def BUN(opcode, operand):
            ...
            # if opcode == 0X4:
            #     pass
            # else:
            #     operand = self.memory_read(operand)    

            # AR = self.register_read("AR")
            # self.register_write({"PC": AR})
            
        
        def BSA(opcode, operand):
            ...
            # if opcode == 0X5:
            #     pass
            # else:
            #     operand = self.memory_read(operand)    

            # PC = self.register_read("PC")
            # self.memory_write({operand: PC})
            # AR = self.register_read("AR")
            # self.register_write({"PC": AR})              


        def ISZ(opcode, operand):
            ...
            # if opcode == 0X6:
            #     pass
            # else:
            #     operand = self.memory_read(operand)
            
            # value = self.memory_read(operand)
            # value = (value + 1) & 0xFFFF 
            # self.memory_write(operand, value)
            
            # if value == 0:
            #     PC = self.register_read("PC")
            #     self.register_write({"PC": PC + 1})


        print("memory based")
        if opcode == "0x0" or opcode == "0x8":
            print("AND")
            AND(opcode, operand) 
        elif opcode == "0x1" or opcode == "0x9":
            print("ADD")
            ADD(opcode, operand) 
        elif opcode == "0x2" or opcode == "0xA":
            print("LDA")
            LDA(opcode, operand) 
        elif opcode == "0x3" or opcode == "0xB":
            print("STA")
            STA(opcode, operand) 
        elif opcode == "0x4" or opcode == "0xC":
            print("BUN")
            BUN(opcode, operand) 
        elif opcode == "0x5" or opcode == "0xD":
            print("BSA")
            BSA(opcode, operand) 
        elif opcode == "0x6" or opcode == "0xE":
            print("ISZ")
            ISZ(opcode, operand) 

        




def main():
    c = Core()
    c.register_write({"AC": 0x1})
    c.register_write({"E": 0x0})
    # ["0 ADD 74f", "1 BSA 54C", "0 ISZ 001", "CLA", "HLT", "INC", "SZA"]
    c.compile([])
    c.fetch_and_decode()

    



if __name__ == "__main__":
    main()