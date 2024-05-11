from dataclasses import dataclass


@dataclass
class PrBaseException(Exception):
    """
    Base class for exceptions in this project.
    """
    status : int = 400
    message : str = "An error occurred."
