#! usr/bin/python
def memory_write(self, data: dict) -> None:
    """
    set a memory value in a single given address
    example input: `data = {address: 0XFE, value: 0X12}`
    """
    ...


def memory_bulk_write(self, data: list[dict]) -> None:
    """
    set memory values in multiple given addresses
    example input: `data = [ {address: 0XFE, value: 0X12}, {address: 0XFF, value: 0X13} ]`
    """
    ...


def memory_bulk_read(self) -> list[dict]:
    """
    return a list of memory values
    example output: `data = [ {address: 0XFE, value: 0X12}, {address: 0XFF, value: 0X13} ]`
    """
    ...


def memory_read(self, address) -> dict:
    """
    return a dictionary of memory value in a given address
    example input: `address= "0XFE"`
    example output: `data = {address: 0XFE, value: 0X12}`
    """
    ...


def register_write(self, data: dict[str, str]) -> None:
    """
    Write data to the register.
    example input: `data = {"TC": "0X12, "E":"0XF"}`
    """
    ...


def register_read(self) -> dict[str, str]:
    """
    return a dictionary of register values
    example: `data = {"TC": "0X12, "E":"0XF", ...}`
    be careful to return values of all registers.
    such as `TC`, `E`, `PC`, `IR`, `AR`, `DR`, `AC`, `E`
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
