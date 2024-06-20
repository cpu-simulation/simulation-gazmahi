#! usr/bin/python
from pprint import pprint


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
        """compiles given code line sinto machine codes

        Args:
            instructions (list[str]): the code lines(a.k. instructions)

        Returns:
            list[str]: the compiled code(a.k. machine code instructions)
        """
        

        # the list that contains the machine code of the input list of instructions
        machine_code_instruction = []

        # a counter for controling the errors
        instruction_line = 0
        for instruct in instructions:
                

                instruction_line += 1


                # compiling memory reference instructions
                # convert them to macine code


                if "ADD" in instruct:
                    try:
                        ar = instruct[6: ]
                        if instruct[0] == "0":
                            machine_code_instruction.append("0X0" + ar)
                        elif instruct[0] == "1":
                            machine_code_instruction.append("0X8" + ar) 
                        else:
                            raise ValueError(f"Wrong Instructions: in the line {instruction_line}")
                    except Exception:
                        raise ValueError(f"Wrong Instructions: in the line {instruction_line}")
                if "AND" in instruct:
                    try:
                        ar = instruct[6: ]
                        if instruct[0] == "0":
                            machine_code_instruction.append("0X1" + ar)
                        elif instruct[0] == "1":
                            machine_code_instruction.append("0X9" + ar) 
                        else:
                            raise ValueError(f"Wrong Instructions: in the line {instruction_line}")
                    except Exception:
                        raise ValueError(f"Wrong Instructions: in the line {instruction_line}")
                if "LDA" in instruct:
                    try:
                        ar = instruct[6: ]
                        if instruct[0] == "0":
                            machine_code_instruction.append("0X2" + ar)
                        elif instruct[0] == "1":
                            machine_code_instruction.append("0XA" + ar) 
                        else:
                            raise ValueError(f"Wrong Instructions: in the line {instruction_line}")
                    except Exception:
                        raise ValueError(f"Wrong Instructions: in the line {instruction_line}")
                if "STA" in instruct:
                    try:
                        ar = instruct[6: ]
                        if instruct[0] == "0":
                            machine_code_instruction.append("0X3" + ar)
                        elif instruct[0] == "1":
                            machine_code_instruction.append("0XB" + ar) 
                        else:
                            raise ValueError(f"Wrong Instructions: in the line {instruction_line}")
                    except Exception:
                        raise ValueError(f"Wrong Instructions: in the line {instruction_line}")
                if "BUN" in instruct:
                    try:
                        ar = instruct[6: ]
                        if instruct[0] == "0":
                            machine_code_instruction.append("0X4" + ar)
                        elif instruct[0] == "1":
                            machine_code_instruction.append("0XC" + ar) 
                        else:
                            raise ValueError(f"Wrong Instructions: in the line {instruction_line}") 
                    except Exception:
                        raise ValueError(f"Wrong Instructions: in the line {instruction_line}")
                if "BSA" in instruct:
                    try:
                        ar = instruct[6: ]
                        if instruct[0] == "0":
                            machine_code_instruction.append("0X5" + ar)
                        elif instruct[0] == "1":
                            machine_code_instruction.append("0XD" + ar) 
                        else:
                            raise ValueError(f"Wrong Instructions: in the line {instruction_line}")
                    except Exception:
                        raise ValueError(f"Wrong Instructions: in the line {instruction_line}")
                if "ISZ" in instruct:
                    try:
                        ar = instruct[6: ]
                        if instruct[0] == "0":
                            machine_code_instruction.append("0X4" + ar)
                        elif instruct[0] == "1":
                            machine_code_instruction.append("0XF" + ar) 
                        else:
                            raise ValueError(f"Wrong Instructions: in the line {instruction_line}")
                    except Exception:
                        raise ValueError(f"Wrong Instructions: in the line {instruction_line}")
                    
                # compiling register reference instructions
                # convert them to macine code
                
                if "CLA" in instruct:
                    try:
                        if len(instruct) == 3:
                            machine_code_instruction.append("0X7800")
                        else:
                            raise ValueError(f"Wrong Instructions: in the line {instruction_line}")
                    except Exception:
                        raise ValueError(f"Wrong Instructions: in the line {instruction_line}")
                if "CLE" in instruct:
                    try:
                        if len(instruct) == 3:
                            machine_code_instruction.append("0X7400")
                        else:
                            raise ValueError(f"Wrong Instructions: in the line {instruction_line}")
                    except Exception:
                        raise ValueError(f"Wrong Instructions: in the line {instruction_line}")
                if "CMA" in instruct:
                    try:
                        if len(instruct) == 3:
                            machine_code_instruction.append("0X7200")
                        else:
                            raise ValueError(f"Wrong Instructions: in the line {instruction_line}")
                    except Exception:
                        raise ValueError(f"Wrong Instructions: in the line {instruction_line}")
                if "CME" in instruct:
                    try:
                        if len(instruct) == 3:
                            machine_code_instruction.append("0X7100")
                        else:
                            raise ValueError(f"Wrong Instructions: in the line {instruction_line}")
                    except Exception:
                        raise ValueError(f"Wrong Instructions: in the line {instruction_line}")
                if "CIR" in instruct:
                    try:
                        if len(instruct) == 3:
                            machine_code_instruction.append("0X7080")
                        else:
                            raise ValueError(f"Wrong Instructions: in the line {instruction_line}")
                    except Exception:
                        raise ValueError(f"Wrong Instructions: in the line {instruction_line}")
                if "CIL" in instruct:
                    try:
                        if len(instruct) == 3:
                            machine_code_instruction.append("0X7040")
                        else:
                            raise ValueError(f"Wrong Instructions: in the line {instruction_line}")
                    except Exception:
                        raise ValueError(f"Wrong Instructions: in the line {instruction_line}")
                if "INC" in instruct:
                    try:
                        if len(instruct) == 3:
                            machine_code_instruction.append("0X7020")
                        else:
                            raise ValueError(f"Wrong Instructions: in the line {instruction_line}")
                    except Exception:
                        raise ValueError(f"Wrong Instructions: in the line {instruction_line}")
                if "SPA" in instruct:
                    try:
                        if len(instruct) == 3:
                            machine_code_instruction.append("0X7010")
                        else:
                            raise ValueError(f"Wrong Instructions: in the line {instruction_line}")
                    except Exception:
                        raise ValueError(f"Wrong Instructions: in the line {instruction_line}")
                if "SNA" in instruct:
                    try:
                        if len(instruct) == 3:
                            machine_code_instruction.append("0X7008")
                        else:
                            raise ValueError(f"Wrong Instructions: in the line {instruction_line}")
                    except Exception:
                        raise ValueError(f"Wrong Instructions: in the line {instruction_line}")
                if "SZA" in instruct:
                    try:
                        if len(instruct) == 3:
                            machine_code_instruction.append("0X7004")
                        else:
                            raise ValueError(f"Wrong Instructions: in the line {instruction_line}")
                    except Exception:
                        raise ValueError(f"Wrong Instructions: in the line {instruction_line}")
                if "SZE" in instruct:
                    try:
                        if len(instruct) == 3:
                            machine_code_instruction.append("0X7002")
                        else:
                            raise ValueError(f"Wrong Instructions: in the line {instruction_line}")
                    except Exception:
                        raise ValueError(f"Wrong Instructions: in the line {instruction_line}")
                if "HLT" in instruct:
                    try:
                        if len(instruct) == 3:
                            machine_code_instruction.append("0X7001")
                        else:
                            raise ValueError(f"Wrong Instructions: in the line {instruction_line}")
                    except Exception:
                        raise ValueError(f"Wrong Instructions: in the line {instruction_line}")
                    
                # compiling INP/OUT reference instructions
                # convert them to macine code

                if "INP" in instruct:
                    try:
                        if len(instruct) == 3:
                            machine_code_instruction.append("0X7800")
                        else:
                            raise ValueError(f"Wrong Instructions: in the line {instruction_line}")
                    except Exception:
                        raise ValueError(f"Wrong Instructions: in the line {instruction_line}")
                if "OUT" in instruct:
                    try:
                        if len(instruct) == 3:
                            machine_code_instruction.append("0X7400")
                        else:
                            raise ValueError(f"Wrong Instructions: in the line {instruction_line}")
                    except Exception:
                        raise ValueError(f"Wrong Instructions: in the line {instruction_line}")
                if "SKI" in instruct:
                    try:
                        if len(instruct) == 3:
                            machine_code_instruction.append("0X7200")
                        else:
                            raise ValueError(f"Wrong Instructions: in the line {instruction_line}")
                    except Exception:
                        raise ValueError(f"Wrong Instructions: in the line {instruction_line}")
                if "SKO" in instruct:
                    try:
                        if len(instruct) == 3:
                            machine_code_instruction.append("0X7100")
                        else:
                            raise ValueError(f"Wrong Instructions: in the line {instruction_line}")
                    except Exception:
                        raise ValueError(f"Wrong Instructions: in the line {instruction_line}")
                if "ION" in instruct:
                    try:
                        if len(instruct) == 3:
                            machine_code_instruction.append("0X7080")
                        else:
                            raise ValueError(f"Wrong Instructions: in the line {instruction_line}")
                    except Exception:
                        raise ValueError(f"Wrong Instructions: in the line {instruction_line}")
                if "IOF" in instruct:
                    try:
                        if len(instruct) == 3:
                            machine_code_instruction.append("0X7001")
                        else:
                            raise ValueError(f"Wrong Instructions: in the line {instruction_line}")
                    except Exception:
                        raise ValueError(f"Wrong Instructions: in the line {instruction_line}")
        
        return machine_code_instruction
                

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



                    

                    
    
    def execute_instruction(self) -> None:
        """
        execute saved instructions
        """
        ...






def main():
    c = Core()
    c.memory_bulk_write([{"0XFE": "0X12"}, {"0XFF": "0X13"}])
    c.memory_bulk_read()
    c.compile(["0 ADD 74f", "1 BSA 54C", "0 ISZ 001", "CLA", "HLT", "INC", "SZA"])
    print(c.memory)

    



if __name__ == "__main__":
    main()