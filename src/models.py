#! usr/bin/python
"""
HELP:
write classes ypu need in here.
i've been writing some of them but they are not completed
for example:
    write a class 'Core' with inheritance from BaseCore 
    dont forget to import it in __init__.py file as Core

"""

from abc import ABC, abstractmethod
from .errors import PrBaseException

class BaseMemory(ABC):

    @abstractmethod
    def set(self, data: dict)-> None:
        ...

    @property
    @abstractmethod
    def read(self)-> dict:
        ...
class BaseRegister(ABC):

    @abstractmethod
    def set(self, data:dict) -> None:
        ...

    @property
    @abstractmethod
    def read(self)-> dict:
        ...

class BaseCore(ABC):

    memory: BaseMemory = ...
    registers: BaseRegister = ... 

    @abstractmethod
    def execute_instruction(self, instruction:dict):
        ...