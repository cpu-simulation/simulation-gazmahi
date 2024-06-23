def compiler(instructions):
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