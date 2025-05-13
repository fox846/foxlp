#que 19
import re

def generate_mnt_and_mdt(code):
    # Initialize MNT and MDT
    mnt = []
    mdt = []

    # Split the code into lines for easier processing
    lines = code.splitlines()

    # Variables to track macro definitions
    current_macro = None
    mdt_index = 0  # Tracks the starting index for each macro in MDT
    macro_start_index = {}  # Tracks where each macro starts in MDT

    # First pass: Generate MNT and MDT
    for line in lines:
        line = line.strip()

        # Identify MACRO definition and extract name and parameters
        macro_match = re.match(r"MACRO\s+(\w+)(\s+(\w+(\s*,\s*\w+)*))?", line) 

# MACRO\s+ → Matches the word MACRO followed by one or more spaces.
# (\w+) → Captures the macro name (e.g., ADD5)
# (\s+(\w+(\s*,\s*\w+)*))? → Optionally captures parameters like A1, A2, A3

        if macro_match:
# line = "MACRO ADD5 A1, A2, A3"
# macro_match.group(1) → "ADD5"
# macro_match.group(3) → "A1, A2, A3"

            macro_name = macro_match.group(1)
            params = macro_match.group(3)
            params_list = [param.strip() for param in params.split(',')] if params else []

            # Add to MNT: (macro name, number of parameters, starting index of MDT)
            macro_start_index[macro_name] = mdt_index
            mnt.append((macro_name, len(params_list), mdt_index))

            # Start the macro body in MDT without the macro header (just instructions)
            current_macro = macro_name
            continue

        # Process macro body or other instructions
        if current_macro:
            if line == "MEND":
                mdt.append(f"({mdt_index}) {line}")  # Add the MEND statement with index
                mdt_index += 1
                current_macro = None
                continue
            # Add the macro body to MDT (instructions inside the macro)
            mdt.append(f"({mdt_index}) {line}")  # Add the line with its index
            mdt_index += 1

    # Remove the calls and instances like SRS and ADD1 C1, C2, C3 from MDT
    mdt_cleaned = []
    for line in mdt:
        if not line.startswith("SRS") and not line.startswith("ADD1"):
            mdt_cleaned.append(line)

    return mnt, mdt_cleaned

# Example code input
code = """
LOAD J
STORE M
MACRO EST1
LOAD e
ADD d
MEND
MACRO EST ABC
EST1
STORE ABC
MEND
MACRO ADD7 P4, P5, P6
LOAD P5
EST 8
SUB4 2
STORE P4
STORE P6
MEND
EST
ADD7 C4, C5, C6
END
"""

mnt, mdt = generate_mnt_and_mdt(code)

# Print MNT (Macro Name Table)
print("Macro Name Table (MNT):")
print("Name of Macro | No. of Parameters | Starting Index of MDT")
for entry in mnt:
    print(f"{entry[0]:<15} | {entry[1]:<17} | {entry[2]}")

# Print the cleaned MDT (Macro Definition Table) with no macro name at the start
print("\nMacro Definition Table (MDT):")
for line in mdt:
    print(line)
