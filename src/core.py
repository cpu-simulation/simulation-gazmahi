from compiler import compiler
from components import *

class Core:
    def __init__(self) -> None:
        # our mrmory object
        # placing our components on the core
        self.memory = Memory()

        self.registers = [] # container for register objects
        # making objects and adding them to the self.registers
        for i,j in [("AC",16),("IR",16),("AR", 12),("DR",16),("INPR",8),("PC", 12),("OUTR",8),("TR",16),("E",1)]:
            reg = Register(i, j)
            self.registers.append(reg)

        # ALU object
        self.ALU = ALU()


    # ------- methdos for registers and memory --------
    def memory_write(self, data: dict[int: str]) -> None:
        for key, value in data.items():
            self.memory.write(key, value)


    def memory_bulk_write(self, data: list[dict[int: str]]) -> None:
        for cell in data:
            self.memory_write(cell)
    
    
    def memory_bulk_read(self) -> None:
        self.memory.bulk_read()
        
    
    
    def memory_read(self, address: int) -> dict:
        if isinstance(address, int):
            if 0 <= address <= 4095:
                return self.memory.read(address)
            else:
                raise ValueError(f"invalid cell address")
        else:
            raise ValueError(f"invalid cell address")
        

  
        
    def register_write(self, data: dict[str, int]) -> None:
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



    # ----------- compiling the instructions -------------

    @staticmethod
    def compiling_instructions(instructions: list[str]) -> list[str]:
        return compiler(instructions)



    def save_in_memorry(self, machinecode: list[str]) -> None:
        """save the machine codes in the memory cells of the object(a.k. self.memory)

        Args:
            machinecode (list[str]): the list of machine codes instructions
        """

        # saving the codes in the first cells of the memory
        ar = 0
        for code in machinecode:
            self.memory.write(ar, code)
            ar += 1

 
    def compile(self, instructions: list[str]) -> None:
        self.machine_code_instrucions =  self.compiling_instructions(instructions)
        self.save_in_memorry(self.machine_code_instrucions)




    # ----------- execution of machinecodes stored in memory --------------
    def fetch_and_decode(self):   
        print(self.machine_code_instrucions)     
        while True:
            self.PC = self.register_read("PC") # an integer

            # storing PC in AR register 
            self.register_write({"AR": self.PC})
            AR = self.register_read("AR") # an integer

            # retrieving address register through PC number
            IR = self.memory.read(AR) # EX: "0X4001"
            self.register_write({"IR": IR})


            # checsk if we reached the END instruction
            # END instruction -> 0x0 or 0 as decimal integer
            int_IR = int(IR, 16)
            if int_IR == 0:
                break

            # PC incremention
            self.PC += 1
            self.register_write({"PC": self.PC})

            # decoding
            opcode = (self.ALU.And(IR, 0XF000)) # EX: "0x4000"
            opcode = self.ALU.Rshift(opcode , 12) # EX: "0X4"
            operand = self.ALU.And(IR, 0X0FFF) # EX: "0X1" or "0X800"

            # chossing the proper function
            # DOESN'T include INP/OUT instructions
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
            print("CLE")
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
            if opcode == "0x0":
                pass
            else:
                operand = self.memory_read(int(operand, 16))

            operand = int(operand, 16)

            # storing in operand in data register
            self.register_write({"DR": operand})
            DR = self.register_read("DR")

            # And operation on the AC
            AC = self.register_read("AC")
            self.register_write({"AC": self.ALU.And(AC, DR)}) # AC & DR

            self.registers_info()
            self.memory_bulk_read()

        
        def ADD(opcode, operand):
            print(opcode, operand)
            if opcode == "0x1":
                pass
            else:
                operand = self.memory_read(int(operand, 16))

            # storing in operand in data register
            operand = int(operand, 16)

            # storing in operand in data register
            self.register_write({"DR": operand})
            DR = self.register_read("DR")

            # ADD operation in AC
            AC = self.register_read("AC")
            result, carry = self.ALU.Add(AC, DR)
            self.register_write({"AC": result})
            self.register_write({"E": carry})

            self.registers_info()
            self.memory_bulk_read()
            

        def LDA(opcode, operand):
            print(opcode, operand)
            if opcode == "0x2":
                pass
            else:
                operand = self.memory_read(int(operand, 16))
            # storing in operand in data register
            operand = int(operand, 16)
            self.register_write({"DR": operand})
            DR = self.register_read("DR")

            # searching for the value
            self.register_write({"AR": DR})
            AR = self.register_read("AR")            
            value = self.memory_read(AR)

            # writing the value in the accumulator
            self.register_write({"AC": value})

            self.registers_info()
            self.memory_bulk_read()


        def STA(opcode, operand):
            print(opcode, operand)
            if opcode == "0x3":
                pass
            else:
                operand = self.memory_read(int(operand, 16))
            # storing in operand in data register
            operand = int(operand, 16)
            self.register_write({"DR": operand})
            DR = self.register_read("DR")

            # storing accumulator
            AC = self.register_read("AC")
            self.memory_write({DR: AC})

            self.registers_info()
            self.memory_bulk_read()


        def BUN(opcode, operand):
            if opcode == "0x4":
                pass
            else:
                operand = self.memory_read(int(operand, 16)) 

            # storing in operand in data register
            operand = int(operand, 16)
            self.register_write({"DR": operand})
            DR = self.register_read("DR")

            # changing the PC
            self.register_write({"PC": DR})

            self.registers_info()
            self.memory_bulk_read()
            
        
        def BSA(opcode, operand):
            print(operand, type(operand))
            if opcode == "0x5":
                pass
            else:
                operand = self.memory_read(int(operand, 16)) 
                
            # storing in operand in data register
            operand = int(operand, 16)
            print(operand, type(operand))
            self.register_write({"DR": operand})
            DR = self.register_read("DR")

            # stoing the address
            self.register_write({"AR": DR})
            AR = self.register_read("AR")

            # access to PC value
            self.PC = self.register_read("PC")
            PC = hex(self.PC)

            # writing the PC in the address
            self.memory_write({AR: PC})

            # the new PC
            PC = self.ALU.Inc(AR)
            PC = int(PC, 16)
            self.register_write({"PC": PC})

            self.registers_info()
            self.memory_bulk_read()


        def ISZ(opcode, operand):
            if opcode == "0x6":
                pass
            else:
                operand = self.memory_read(int(operand, 16))  
            

            # storing in operand in data register
            operand = int(operand, 16)
            self.register_write({"DR": operand})
            DR = self.register_read("DR")


            value = self.memory_read(operand)
            value = self.ALU.Inc(value) # value + 1 
            self.memory_write({DR: value})


            print(value, type(value))
            if int(value, 16) == 0:
                PC = self.register_read("PC")
                PC += 1
                self.register_write({"PC": PC}) 

            self.registers_info()
            self.memory_bulk_read()



        print("memory based")
        if opcode == "0x0" or opcode == "0x8":
            print("AND")
            AND(opcode, operand) 
        elif opcode == "0x1" or opcode == "0x9":
            print("ADD")
            ADD(opcode, operand) 
        elif opcode == "0x2" or opcode == "0xa":
            print("LDA")
            LDA(opcode, operand) 
        elif opcode == "0x3" or opcode == "0xb":
            print("STA")
            STA(opcode, operand) 
        elif opcode == "0x4" or opcode == "0xc":
            print("BUN")
            BUN(opcode, operand) 
        elif opcode == "0x5" or opcode == "0xd":
            print("BSA")
            BSA(opcode, operand) 
        elif opcode == "0x6" or opcode == "0xe":
            print("ISZ")
            ISZ(opcode, operand) 

        

def main():
    # example
    c = Core()
    c.memory_write({0x70: "0x49", # 0x49 = 73
                    74: "0x1132", # -> ADD instruction
                    75: "0x0fff",  # -> AND instruction
                    76: "0xC049", # indirect BUN to (0x49 = 73)

                    # using this variable for looping
                    # with ISZ and BUN
                    0x90: "-1",   

                    # Saving data
                    0x100: "-1",
                    0x101: "0xffff",
                    0x102 : "0x5b13"
                    })
    c.compile([
                "1 BSA 70", # indirect BSA to (0x70)th cell of memory

                # ----- demonstrating skip instructions for AC ---
                "CLA",
                "INC", # AC > 0
                "SPA",
                "INC", # skiping
                "CLA",
                "SZA", # AC = 0 
                "INC", # skiping
                "0 LDA 100", # AC < 0 | -> LDA instruction
                "SNA",
                "INC", # skiping

                # ---------- demonstrating E instructions ------
                # making carry
                "0 LDA 101", # -> LDA instruction
                "0 ADD 1", # -> ADD instruction
                # instructions
                "CME", # complement E
                "CLE", # clear E

                # ------ demonstrating AC instructions -------
                "0 LDA 102",
                "CMA",
                "CIR",
                "CIL",

                
                "0 STA 60", # -> STA instruction
                
                # loop making
                # amount of looping = -(value in the 0x90)
                "0 ISZ 90", #  -> ISZ instruction
                "0 BUN 0", # -> BUN instruction
                "END"
                ])

    # "0 LDA 100", "INC", "0 STA 101"
    c.fetch_and_decode()


    

if __name__ == "__main__":
    main()