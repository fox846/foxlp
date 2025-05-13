
#que 17
assembly_code = [
     "STORE P",
    "LOAD Q",
    "MACRO PCG",
    "LOAD m",
    "ADD n",
    "MEND",
    "MOV S",
    "MACRO ADDi PAR",
    "LOAD A",
    "STORE PAR",
    "MEND",
    "DIV B",
    "MACRO ADDii V1, V2, V3",
    "STORE V2",
    "ADDi 12",
    "ADDi 7",
    "LOAD V1",
    "LOAD V3",
    "MEND",
    "PCG",
    "ADDii Q1, Q2, Q3",
    "END"
]

mdt = []
inside_macro = False
arg_map = {}
macro_name = ""
line_number = 1  # For numbering instructions (excluding macro name comment)

for line in assembly_code:
    parts = line.strip()

    if not parts:
        continue

    if parts.startswith("MACRO"):
        inside_macro = True
        macro_header = parts.split() #"MACRO ADD1 ARG" → ['MACRO', 'ADD1', 'ARG']
        macro_name = macro_header[1]
        args = []

        # Extract parameters if available
        if len(macro_header) > 2:
            args = [arg.strip() for arg in ' '.join(macro_header[2:]).split(',')]
        elif ',' in macro_name:  # Handle cases like MACRO ADD5 A1, A2, A3
            macro_name, *args = macro_name.split(',')
            macro_name = macro_name.strip()
            args = [arg.strip() for arg in args]

        arg_map = {arg: f"#" + str(i + 1) for i, arg in enumerate(args)}
        # arg_map = {'A1': '#1', 'A2': '#2', 'A3': '#3'}

        mdt.append(f"; {macro_name}")  # Comment without line number

    elif parts == "MEND":
        mdt.append(f"{line_number}\tMEND")
        line_number += 1
        inside_macro = False
        arg_map = {}
    elif inside_macro:
        parts = parts.split()
        replaced_parts = []
        for part in parts:
            if part in arg_map:
                # If arg_map = {'A1': '#1'} and parts = ['STORE', 'A1']
                replaced_parts.append(arg_map[part])
            else:
                replaced_parts.append(part)
                # replaced_parts = ['STORE', '#1']
        new_line = " ".join(replaced_parts)
        mdt.append(f"{line_number}\t{new_line}")
        line_number += 1

# Output MDT
print("Macro Definition Table (MDT):\n")
for line in mdt:
    print(line)
