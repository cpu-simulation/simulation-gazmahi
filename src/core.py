#! usr/bin/python
from pprint import pprint



class Core:
    def __init__(self) -> None:
        self.memory = []
        self.registers = [{"AC": 0X0000}, {"IR": 0X0000}, {"AR": 0X000}, {"DR": 0X0000}, {"INPR": 0X00}, {"PC": 0X000}, {"OUTR": 0X00}, {"TR": 0X0000}, {"E": 0}]


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


    
    def compile(self, instructions: list[str]) -> None:
    
    
    def execute_instruction(self) -> None:
        """
        execute saved instructions
        """
        ...






def main():
    c = Core()
    c.memory_bulk_write([{0XFE: 0X12}, {0XFF: 0X13}])
    c.memory_bulk_read()

    



if __name__ == "__main__":
    main()