#! usr/bin/python
from pprint import pprint

class Core:
    def __init__(self) -> None:
        self.memory = []
        self.register = [{"AC": 0X00}, {"IR": 0X00}, {"AR": 0X00}, {"DR": 0X00}, {"INPR": 0X00}, {"PC": 0X00}, {"OUTR": 0X00}, {"TR": 0X00}, {"E": 0X00}]

    def memory_write(self, data: dict) -> None:
        """
        set a memory value in a single given address
        example input: `data = {address: 0XFE, value: 0X12}`
        """
        if data not in self.memory:
            self.memory.append(data)

    
    def memory_bulk_write(self, data: list[dict]) -> None:
        """
        set memory values in multiple given addresses
        example input: `data = [ {address: 0XFE, value: 0X12}, {address: 0XFF, value: 0X13} ]`
        """
        for item in data:
            if item not in self.memory:
                self.memory.append(item)        
    
    
    def memory_bulk_read(self) -> list[dict]:
        """
        return a list of memory values
        example output: `data = [ {address: 0XFE, value: 0X12}, {address: 0XFF, value: 0X13} ]`
        """
        print("-" * 30)
        for item in self.memory:
            print(f"address {self.memory.index(item)}:  {list(item.keys())[0]}\nvalue: {list(item.values())[0]}")
        print("-" * 30)
        
    
    
    def memory_read(self, address) -> dict:
        """
        return a dictionary of memory value in a given address
        example input: `address= "0XFE"`
        example output: `data = {address: 0XFE, value: 0X12}`
        """
        for item in self.memory:
            if item.get(address):
                return  f"address:  {list(item.keys())[0]}\nvalue: {list(item.values())[0]}" 
    
    
    def register_write(self, data: dict[str, str]) -> None:
        """
        Write data to the register.
        example input: `data = {"TR": "0X12", "E":"0XF"}`
        """
        for item in self.register:
            if list(item.keys())[0]=="TR":
                item["TR"] = data["TR"]
            if list(item.keys())[0]=="AR":
                item["AR"] = data["AR"]
            if list(item.keys())[0]=="AC":
                item["AC"] = data["AC"]
            if list(item.keys())[0]=="DR":
                item["DR"] = data["DR"]
            if list(item.keys())[0]=="INPR":
                item["INPR"] = data["INPR"]
            if list(item.keys())[0]=="PC":
                item["PC"] = data["PC"]
            if list(item.keys())[0]=="OUTR":
                item["OUTR"] = data["OUTR"]
            if list(item.keys())[0]=="IR":
                item["IR"] = data["IR"]

    
    
    def register_read(self) -> dict[str, str]:
        """
        return a dictionary of register values
        example: `data = {"TR": "0X12, "E":"0XF", ...}`
        be careful to return values of all registers.
        such as `TR`, `E`, `PC`, `IR`, `AR`, `DR`, `AC`, `E`
        """
        ...
    
    
    def compile(self, instructions: list[str]) -> None:
        """
        compile instructions into machine code and save them in memory
        """
        ...
    
    
    def execute_instruction(self) -> None:
        """
        execute saved instructions
        """
        ...



def main():
    c = Core()
    c.memory_bulk_write([{0XFE: 0X12}, {0XFF: 0X13}])
    c.memory_bulk_read()
    c.register_write({"TR": "0X12", "E":"0XF"})
    print(c.register)

    



if __name__ == "__main__":
    main()