#! usr/bin/python
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
