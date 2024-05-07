#! usr/bin/python
from abc import ABC, abstractmethod
from .errors import PrBaseException
from dataclasses import dataclass

class BaseMemory(ABC):

    @abstractmethod
    def set(self, data: list[dict])-> None:
        ...

    @property
    @abstractmethod
    def read(self)-> list[dict]:
        ...

        
class BaseRegister(ABC):

    @abstractmethod
    def set(self, data:dict[str, str]) -> None:
        ...

    @property
    @abstractmethod
    def read(self)-> dict[str, str]:
        ...

class BaseCore(ABC):

    memory: BaseMemory = ...
    registers: BaseRegister = ... 

    @abstractmethod
    def execute_instruction(self, instruction:list[str])-> None:
        ...
