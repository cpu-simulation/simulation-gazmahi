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
        self.memory = Memory()
        self.registers = [] # container for registers objects
        # making objects and adding them to the self.registers
        for i,j in [("AC",16),("IR",16),("AR",16),("DR",16),("INPR",16),("PC",16),("OUTR",16),("TR",16),("E",1)]:
            reg = Register(i, j)
            self.registers.append(reg)


    def registers_info(self):
        print("-" * 40)
        for reg in self.registers:
            reg.info()      
        print("-" * 40)


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
        for label, value in data:
            for reg in self.registers:
                if reg.name == label:
                    reg.write(value)
                else:
                    raise ValueError(f"there is no register with {label} name")

    
    
    def register_read(self, reg_name: str) -> int: 
        for reg in self.registers:
            if reg.name == reg_name:
                return reg.read()
            else:
                raise ValueError(f"there is not a register named: {reg_name}")


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
        self.memory_bulk_read()

 
    def compile(self, instructions: list[str]) -> None:
        machine_code_instrucions =  self.compiling_instructions(instructions)
        self.save_in_memorry(machine_code_instrucions)



    def fetch_and_decode(self):
        PC = self.register_read("PC")
        self.register_write({"AR": PC})
        
        self.carry = False
        self.zero = False
        while True:
            IR = self.memory.read(PC)
            self.register_write({"PC": PC + 1})
            opcode = (IR & 0XF000) >> 12
            operand = IR & 0X0FFF

            if opcode == 0X7:
                self.register_based_instruction(operand)
            else:
                self.memory_based_instruction(opcode, operand)


    def register_based_instruction(self, operand):
        if operand == 0X7800:
            CLA()
        elif operand == 0X7400:
            CLE()
        elif operand == 0X7200:
            CMA()
        elif operand == 0X7100:
            CME()
        elif operand == 0X7080:
            CIR()
        elif operand == 0X7040:
            CIL()
        elif operand == 0X7020:
            INC()
        elif operand == 0X7010:
            SPA()
        elif operand == 0X7008:
            SNA()
        elif operand == 0X7004:
            SZA()
        elif operand == 0X7002:
            SZE()
        elif operand == 0X7001:
            HLT()
            
        def CLA():
            self.register_write({"AC": 0})

        def CLE():
            self.register_write({"E": 0})

        def CMA():
            AC = self.register_read("AC")
            self.register_write({"AC": ~AC & 0xFFFF}) 

        def CME():
            E = self.register_read("E")
            self.register_write({"E": ~E & 0x1}) 

        def CIR():
            AC = self.register_read("AC")
            E = self.register_read("E")
            new_E = (AC & 0x1) 
            AC = (AC >> 1) | (E << 15)  
            self.register_write({"AC": AC})
            self.register_write({"E": new_E})

        def CIL(): 
            AC = self.register_read("AC")
            E = self.register_read("E")
            new_E = (AC >> 15) & 0x1  
            AC = ((AC << 1) & 0xFFFF) | E  
            self.register_write({"AC": AC})
            self.register_write({"E": new_E})

        def INC(): 
            AC = self.register_read("AC")
            self.register_write({"AC": (AC + 1) & 0xFFFF})  

        def SPA():
            AC = self.register_read("AC")
            if AC >= 0:
                PC = self.register_read("PC")
                self.register_write({"PC": PC + 1}) 

        def SNA():
            AC = self.register_read("AC")
            if AC < 0:
                PC = self.register_read("PC")
                self.register_write({"PC": PC + 1})  
                    
        def SZA():
            AC = self.register_read("AC")
            if AC == 0:
                PC = self.register_read("PC")
                self.register_write({"PC": PC + 1}) 

        def SZE():
            E = self.register_read("E")
            if E == 0:
                PC = self.register_read("PC")
                self.register_write({"PC": PC + 1}) 

        def HLT(): 
            raise SystemExit("HALT instruction executed. Stopping the CPU.") 


    def memory_based_instruction(self, opcode, operand):
        if opcode == 0X0 or opcode == 0X8:
            AND(opcode, operand) 
        elif opcode == 0X1 or opcode == 0X9:
            ADD(opcode, operand) 
        elif opcode == 0X2 or opcode == 0XA:
            LDA(opcode, operand) 
        elif opcode == 0X3 or opcode == 0XB:
            STA(opcode, operand) 
        elif opcode == 0X4 or opcode == 0XC:
            BUN(opcode, operand) 
        elif opcode == 0X5 or opcode == 0XD:
            BSA(opcode, operand) 
        elif opcode == 0X6 or opcode == 0XE:
            ISZ(opcode, operand) 

        
        def AND(opcode, operand):
            if opcode == 0X0:
                pass
            else:
                operand = self.memory_read(operand)
            
            self.register_write({"DR": operand})
            DR = self.register_read("DR")
            AC = self.register_read("AC")
            self.register_write({"AC": AC & DR})    

        
        def ADD(opcode, operand):
            if opcode == 0X1:
                pass
            else:
                operand = self.memory_read(operand)

            self.register_write({"DR": operand})
            DR = self.register_read("DR")
            AC = self.register_read("AC")
            result, carry = self.alu.add(AC, DR)
            self.register_write({"AC": result})
            self.register_write({"E": carry})
            
        def LDA(opcode, operand):
            if opcode == 0X2:
                pass
            else:
                operand = self.memory_read(operand)
            
            self.register_write({"DR": operand})
            DR = self.register_read("DR")
            self.register_write({"AC": DR})    



        def STA(opcode, operand):
            if opcode == 0X3:
                pass
            else:
                operand = self.memory_read(operand)
            

            AC = self.register_read("AC")
            self.memory_write({operand: AC})


        def BUN(opcode, operand):
            if opcode == 0X4:
                pass
            else:
                operand = self.memory_read(operand)    

            AR = self.register_read("AR")
            self.register_write({"PC": AR})
            
        
        def BSA(opcode, operand):
            if opcode == 0X5:
                pass
            else:
                operand = self.memory_read(operand)    

        PC = self.register_read("PC")
        self.memory_write({operand: PC})
        AR = self.register_read("AR")
        self.register_write({"PC": AR})              


        def ISZ(opcode, operand):
            if opcode == 0X6:
                pass
            else:
                operand = self.memory_read(operand)
            
            value = self.memory_read(operand)
            value = (value + 1) & 0xFFFF 
            self.memory_write(operand, value)
            
            if value == 0:
                PC = self.register_read("PC")
                self.register_write({"PC": PC + 1})



def main():
    c = Core()
    c.compile(["0 ADD 74f", "1 BSA 54C", "0 ISZ 001", "CLA", "HLT", "INC", "SZA"])
    print(c.memory)

    



if __name__ == "__main__":
    main()