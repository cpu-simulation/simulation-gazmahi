"""
HELP:
write classes ypu need in here.
i've been writing some of them but they are not completed
for example:
    write a class 'Core' with inheritance from BaseCore 
    dont forget to import it in __init__.py file as Core

"""


from abc import ABC, abstractmethod

class BaseMemory(ABC):
    ...

class BaseRegister(ABC):
    ...


class BaseCore(ABC):

    memory : BaseMemory = ...
    registers: BaseRegister = ... 

    @abstractmethod
    def set_register(self):
        ...
    
    @property
    @abstractmethod
    def read_registers(self):
        ...

    @abstractmethod
    def set_memory(self):
        ...
    
    @property
    @abstractmethod
    def read_memory(self):
        ...


