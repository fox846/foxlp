#que 15
# Assembly input with macros
import re
assembly_code = [
    "LOAD F",
    "STORE E",
    "MACRO SRS",
    "LOAD s",
    "SUB t",
    "MEND",
    "STORE k",
    "MACRO ADD3 XYZ",
    "LOAD U",
    "STORE XYZ",
    "MEND",
    "Add m",
    "MACRO ADD1 Si, Sii, Siii",
    "LOAD Sii",
    "ADD3 1",
    "ADD3 11",
    "STORE Si",
    "STORE Siii",
    "MEND",
    "SRS",
    "ADD1 C1, C2, C3",
    "ADD3 q",
    "END"
]

# Pass 1: Store macro definitions
macros = {}
intermediate_code = []
macro_def = []
macro_name = ""
inside_macro = False

for line in assembly_code:
    parts = line.strip().split()
    if not parts:
        continue
    if parts[0] == "MACRO":
        macro_name = parts[1]
        macro_def = []
        inside_macro = True
    elif parts[0] == "MEND":
        macros[macro_name] = macro_def
        inside_macro = False
    elif inside_macro:
        macro_def.append(line.strip())
    else:
        intermediate_code.append(line.strip())

# Helper: Expand macro calls recursively with proper parameter substitution
def expand_macro(line):
    parts = line.strip().split()
    if not parts:
        return [line]

    name = parts[0]

    if name in macros:
        macro_body = macros[name]
        if name == "ADD3":
            param = parts[1]
            return [stmt.replace("XYZ", param) for stmt in macro_body]
        elif name == "ADD1":
            si, sii, siii = parts[1], parts[2], parts[3]
            expanded = []
            for stmt in macro_body:
                replaced = stmt
                replaced = re.sub(r'\bSiii\b', siii, replaced)
                replaced = re.sub(r'\bSii\b', sii, replaced)
                replaced = re.sub(r'\bSi\b', si, replaced)
                if replaced.split()[0] in macros:
                    expanded.extend(expand_macro(replaced))
                else:
                    expanded.append(replaced)
            return expanded
        elif name == "SRS":  
            return macro_body
    return [line]


# Pass 2: Expand macros in intermediate code
final_code = []
for line in intermediate_code:
    expanded = expand_macro(line)
    final_code.extend(expanded)

# Clean commas if any (optional)
final_code = [line.rstrip(',') for line in final_code]

# Output
print("Intermediate Code:")
for line in final_code:
    print(line)
