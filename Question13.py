#que 13
# Assembly code with macros
assembly_code = [
    "LOAD A",
    "MACRO ABC",
    "LOAD p",
    "SUB q",
    "MEND",
    "STORE B",
    "MULT D",
    "MACRO ADD1 ARG",
    "LOAD X",
    "STORE ARG",
    "MEND",
    "LOAD B",
    "MACRO ADD5 A1, A2, A3",
    "STORE A2",
    "ADD1 5",
    "ADD1 10",
    "LOAD A1",
    "LOAD A3",
    "MEND",
    "ADD1 t", #macrocall
    "ABC",
    "ADD5 D1, D2, D3",
    "END" #normal line
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
        if name == "ADD1":
            arg = parts[1]
            return [l.replace("ARG", arg) for l in macro_body]
        elif name == "ADD5":
            a1, a2, a3 = parts[1], parts[2], parts[3]
            expanded = []
            for l in macro_body:
                l = l.replace("A1", a1).replace("A2", a2).replace("A3", a3)
                expanded.extend(expand_line(l))  # Recursively expand nested macros
            return expanded
        elif name == "ABC":
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
