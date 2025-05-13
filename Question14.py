#que 13
# Assembly code with macros
assembly_code = [
   "STORE P",
    "LOAD Q",
    "MACRO PCG",
    "LOAD m",
    "ADD n",
    "MEND",
    "LOAD H",
    "LOAD K",
    "MACRO ADDi PAR",
    "LOAD A",
    "STORE PAR",
    "MEND",
    "DIV R",
    "MACRO ADDii V1, V2, V3",
    "STORE V2",
    "ADDi 12",
    "ADDi 7",
    "LOAD V1",
    "LOAD V3",
    "MEND",
    "PCG",
    "ADDii Q1, Q2, Q3",
    "ADDi w",
    "END"
]

# Storage for macros and their body
macros = {}
macros_in_progress = None
current_macro_name = None

# First pass: Identify macros and store their bodies
intermediate_code = []

for line in assembly_code:
    parts = line.strip().split()
    if not parts:
        continue

    if parts[0] == "MACRO":
        current_macro_name = parts[1]
        macros_in_progress = []
    elif parts[0] == "MEND":
        if macros_in_progress is not None:
            macros[current_macro_name] = macros_in_progress
            macros_in_progress = None
    elif macros_in_progress is not None:
        macros_in_progress.append(line.strip())
    else:
        intermediate_code.append(line.strip())

# Function to recursively expand a line (macro call or normal line)
def expand_line(line):
    parts = line.strip().split()
    if not parts:
        return [line]

    name = parts[0]
    if name in macros:
        macro_body = macros[name]
        if name == "ADDi":
            arg = parts[1]
            return [l.replace("PAR", arg) for l in macro_body]
        elif name == "ADDii":
            v1, v2, v3 = parts[1], parts[2], parts[3]
            expanded = []
            for l in macro_body:
                replaced = l.replace("V1", v1).replace("V2", v2).replace("V3", v3)
                expanded.extend(expand_line(replaced))  # recursively expand if macro inside macro
            return expanded
        elif name == "PCG":
            return macro_body[:]
    return [line]

# Second pass: Expand macros
final_code = []

for line in intermediate_code:
    expanded_lines = expand_line(line)
    final_code.extend(expanded_lines)

# Remove any trailing commas
final_code = [line.rstrip(',') for line in final_code]

# Output the final intermediate code
print("Intermediate Code:")
for line in final_code:
    print(line)




# macros = {
#     'ABC': ["LOAD p", "SUB q"],
#     'ADD1': ["LOAD X", "STORE ARG"],
#     'ADD5': ["STORE A2", "ADD1 5", "ADD1 10", "LOAD A1", "LOAD A3"]
# }

# intermediate_code = [
#     "LOAD A",
#     "STORE B",
#     "MULT D",
#     "LOAD B",
#     "ADD1 t",
#     "ABC",
#     "ADD5 D1, D2, D3",
#     "END"
# ]
