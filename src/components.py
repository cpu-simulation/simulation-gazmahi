from pprint import pprint

class Register:
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.value = 0x0

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
        for add in set(self.active_addresses):
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
        if self.greater_than(result, 0xFFFF): # result > 0xFFFF
            carry = 1
        else:
            carry = 0
        result = self.And(result, 0xFFFF) # result & 0xFFFF
        return result, carry

    def Sub(self, a, b):
        if isinstance(a, str):
            a = int(a, 16)
        if isinstance(b, str):
            b = int(b, 16)       
        result = a - b
        if self.less_than(result, 0): # result < 0
            carry = 1
        else:
            carry = 0
        result = self.And(result, 0xFFFF) # result & 0xFFFF
        return result, carry


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
        result = (a + 1)
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
    
