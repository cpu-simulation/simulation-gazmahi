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


            # ------ compiling memory reference instructions ------
            # convert them to macine code


            if "AND" in instruct:
                try:
                    # slicing our operand out
                    ar = instruct[6: ]

                    # to make sure that out operand's length is 3
                    if len(ar) == 1:
                        ar = "00" + ar
                    elif len(ar) ==2:
                        ar = "0" + ar

                    # if our instruction is direct or indirect
                    if instruct[0] == "0":
                        machine_code_instruction.append("0x0" + ar)
                    elif instruct[0] == "1":
                        machine_code_instruction.append("0x8" + ar) 
                    else:
                        raise ValueError(f"Wrong Instructions: in the line {instruction_line}")
                except Exception:
                    raise ValueError(f"Wrong Instructions: in the line {instruction_line}")
            if "ADD" in instruct:
                try:
                    ar = instruct[6: ]
                    if len(ar) == 1:
                        ar = "00" + ar
                    elif len(ar) ==2:
                        ar = "0" + ar
                    if instruct[0] == "0":
                        machine_code_instruction.append("0x1" + ar)
                    elif instruct[0] == "1":
                        machine_code_instruction.append("0x9" + ar) 
                    else:
                        raise ValueError(f"Wrong Instructions: in the line {instruction_line}")
                except Exception:
                    raise ValueError(f"Wrong Instructions: in the line {instruction_line}")
            if "LDA" in instruct:
                try:
                    ar = instruct[6: ]
                    if len(ar) == 1:
                        ar = "00" + ar
                    elif len(ar) ==2:
                        ar = "0" + ar
                    if instruct[0] == "0":
                        machine_code_instruction.append("0x2" + ar)
                    elif instruct[0] == "1":
                        machine_code_instruction.append("0xA" + ar) 
                    else:
                        raise ValueError(f"Wrong Instructions: in the line {instruction_line}")
                except Exception:
                    raise ValueError(f"Wrong Instructions: in the line {instruction_line}")
            if "STA" in instruct:
                try:
                    ar = instruct[6: ]
                    if len(ar) == 1:
                        ar = "00" + ar
                    elif len(ar) ==2:
                        ar = "0" + ar
                    if instruct[0] == "0":
                        machine_code_instruction.append("0x3" + ar)
                    elif instruct[0] == "1":
                        machine_code_instruction.append("0xB" + ar) 
                    else:
                        raise ValueError(f"Wrong Instructions: in the line {instruction_line}")
                except Exception:
                    raise ValueError(f"Wrong Instructions: in the line {instruction_line}")
            if "BUN" in instruct:
                try:
                    ar = instruct[6: ]
                    if len(ar) == 1:
                        ar = "00" + ar
                    elif len(ar) ==2:
                        ar = "0" + ar
                    if instruct[0] == "0":
                        machine_code_instruction.append("0x4" + ar)
                    elif instruct[0] == "1":
                        machine_code_instruction.append("0xC" + ar) 
                    else:
                        raise ValueError(f"Wrong Instructions: in the line {instruction_line}") 
                except Exception:
                    raise ValueError(f"Wrong Instructions: in the line {instruction_line}")
            if "BSA" in instruct:
                try:
                    ar = instruct[6: ]
                    if len(ar) == 1:
                        ar = "00" + ar
                    elif len(ar) ==2:
                        ar = "0" + ar
                    if instruct[0] == "0":
                        machine_code_instruction.append("0x5" + ar)
                    elif instruct[0] == "1":
                        machine_code_instruction.append("0xD" + ar) 
                    else:
                        raise ValueError(f"Wrong Instructions: in the line {instruction_line}")
                except Exception:
                    raise ValueError(f"Wrong Instructions: in the line {instruction_line}")
            if "ISZ" in instruct:
                try:
                    ar = instruct[6: ]
                    if len(ar) == 1:
                        ar = "00" + ar
                    elif len(ar) ==2:
                        ar = "0" + ar
                    if instruct[0] == "0":
                        machine_code_instruction.append("0x6" + ar)
                    elif instruct[0] == "1":
                        machine_code_instruction.append("0xF" + ar) 
                    else:
                        raise ValueError(f"Wrong Instructions: in the line {instruction_line}")
                except Exception:
                    raise ValueError(f"Wrong Instructions: in the line {instruction_line}")
                
            # ---------- compiling register reference instructions ---------
            # convert them to macine code
            
            if "CLA" in instruct:
                try:
                    if len(instruct) == 3:
                        machine_code_instruction.append("0x7800")
                    else:
                        raise ValueError(f"Wrong Instructions: in the line {instruction_line}")
                except Exception:
                    raise ValueError(f"Wrong Instructions: in the line {instruction_line}")
            if "CLE" in instruct:
                try:
                    if len(instruct) == 3:
                        machine_code_instruction.append("0x7400")
                    else:
                        raise ValueError(f"Wrong Instructions: in the line {instruction_line}")
                except Exception:
                    raise ValueError(f"Wrong Instructions: in the line {instruction_line}")
            if "CMA" in instruct:
                try:
                    if len(instruct) == 3:
                        machine_code_instruction.append("0x7200")
                    else:
                        raise ValueError(f"Wrong Instructions: in the line {instruction_line}")
                except Exception:
                    raise ValueError(f"Wrong Instructions: in the line {instruction_line}")
            if "CME" in instruct:
                try:
                    if len(instruct) == 3:
                        machine_code_instruction.append("0x7100")
                    else:
                        raise ValueError(f"Wrong Instructions: in the line {instruction_line}")
                except Exception:
                    raise ValueError(f"Wrong Instructions: in the line {instruction_line}")
            if "CIR" in instruct:
                try:
                    if len(instruct) == 3:
                        machine_code_instruction.append("0x7080")
                    else:
                        raise ValueError(f"Wrong Instructions: in the line {instruction_line}")
                except Exception:
                    raise ValueError(f"Wrong Instructions: in the line {instruction_line}")
            if "CIL" in instruct:
                try:
                    if len(instruct) == 3:
                        machine_code_instruction.append("0x7040")
                    else:
                        raise ValueError(f"Wrong Instructions: in the line {instruction_line}")
                except Exception:
                    raise ValueError(f"Wrong Instructions: in the line {instruction_line}")
            if "INC" in instruct:
                try:
                    if len(instruct) == 3:
                        machine_code_instruction.append("0x7020")
                    else:
                        raise ValueError(f"Wrong Instructions: in the line {instruction_line}")
                except Exception:
                    raise ValueError(f"Wrong Instructions: in the line {instruction_line}")
            if "SPA" in instruct:
                try:
                    if len(instruct) == 3:
                        machine_code_instruction.append("0x7010")
                    else:
                        raise ValueError(f"Wrong Instructions: in the line {instruction_line}")
                except Exception:
                    raise ValueError(f"Wrong Instructions: in the line {instruction_line}")
            if "SNA" in instruct:
                try:
                    if len(instruct) == 3:
                        machine_code_instruction.append("0x7008")
                    else:
                        raise ValueError(f"Wrong Instructions: in the line {instruction_line}")
                except Exception:
                    raise ValueError(f"Wrong Instructions: in the line {instruction_line}")
            if "SZA" in instruct:
                try:
                    if len(instruct) == 3:
                        machine_code_instruction.append("0x7004")
                    else:
                        raise ValueError(f"Wrong Instructions: in the line {instruction_line}")
                except Exception:
                    raise ValueError(f"Wrong Instructions: in the line {instruction_line}")
            if "SZE" in instruct:
                try:
                    if len(instruct) == 3:
                        machine_code_instruction.append("0x7002")
                    else:
                        raise ValueError(f"Wrong Instructions: in the line {instruction_line}")
                except Exception:
                    raise ValueError(f"Wrong Instructions: in the line {instruction_line}")
            if "HLT" in instruct:
                try:
                    if len(instruct) == 3:
                        machine_code_instruction.append("0x7001")
                    else:
                        raise ValueError(f"Wrong Instructions: in the line {instruction_line}")
                except Exception:
                    raise ValueError(f"Wrong Instructions: in the line {instruction_line}")
                
            # compiling INP/OUT reference instructions
            # convert them to macine code
            # our executer code doesn't include INP/OUT instructions
            # but the compiler compiles and save them in the memory

            if "INP" in instruct:
                try:
                    if len(instruct) == 3:
                        machine_code_instruction.append("0x7800")
                    else:
                        raise ValueError(f"Wrong Instructions: in the line {instruction_line}")
                except Exception:
                    raise ValueError(f"Wrong Instructions: in the line {instruction_line}")
            if "OUT" in instruct:
                try:
                    if len(instruct) == 3:
                        machine_code_instruction.append("0x7400")
                    else:
                        raise ValueError(f"Wrong Instructions: in the line {instruction_line}")
                except Exception:
                    raise ValueError(f"Wrong Instructions: in the line {instruction_line}")
            if "SKI" in instruct:
                try:
                    if len(instruct) == 3:
                        machine_code_instruction.append("0x7200")
                    else:
                        raise ValueError(f"Wrong Instructions: in the line {instruction_line}")
                except Exception:
                    raise ValueError(f"Wrong Instructions: in the line {instruction_line}")
            if "SKO" in instruct:
                try:
                    if len(instruct) == 3:
                        machine_code_instruction.append("0x7100")
                    else:
                        raise ValueError(f"Wrong Instructions: in the line {instruction_line}")
                except Exception:
                    raise ValueError(f"Wrong Instructions: in the line {instruction_line}")
            if "ION" in instruct:
                try:
                    if len(instruct) == 3:
                        machine_code_instruction.append("0x7080")
                    else:
                        raise ValueError(f"Wrong Instructions: in the line {instruction_line}")
                except Exception:
                    raise ValueError(f"Wrong Instructions: in the line {instruction_line}")
            if "IOF" in instruct:
                try:
                    if len(instruct) == 3:
                        machine_code_instruction.append("0x7001")
                    else:
                        raise ValueError(f"Wrong Instructions: in the line {instruction_line}")
                except Exception:
                    raise ValueError(f"Wrong Instructions: in the line {instruction_line}")


            # -------------- END instruction --------------
            if "END" in instruct:
                try:
                    if len(instruct) == 3:
                        machine_code_instruction.append("0x0000")
                    else:
                        raise ValueError(f"Wrong Instructions: in the line {instruction_line}")
                except Exception:
                    raise ValueError(f"Wrong Instructions: in the line {instruction_line}")       
                    
    
    return machine_code_instruction