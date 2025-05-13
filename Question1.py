#Que 1.
# Sample Assembly code lines
assembly_code = [
    "START 100",
    "READ A",
    "READ B",
    "LOOP MOVER AREG, A",
    "     MOVER BREG, B",
    "     COMP BREG, ='2'",
    "     BC GT, LOOP",
    "BACK SUB AREG, B",
    "     COMP AREG, ='5'",
    "     BC LT, BACK",
    "     STOP",
    "A    DS 1",
    "B    DS 1",
    "     END"
]


# instructions (READ, MOVER, COMP, etc.), 
# labels (LOOP, BACK, A, B), 
# directives (START, DS, END), and operands.



# Initialize symbol table and location counter
symbol_table = {}
loc_counter = 0 #LC

# Define set of instructions and directives
keywords = ["START", "END", "READ", "MOVER", "COMP", "BC", "STOP", "DS"]

# Pass 1: Build the symbol table
for line in assembly_code:
    parts = line.strip().split()

# Use strip() to remove leading/trailing spaces 
#  split() to break the line into parts (tokens).

    if len(parts) == 0:  #Skip empty lines, if any.
        continue

    # Handle START directive
    if parts[0] == "START":
        loc_counter = int(parts[1])
        continue

    # Handle END directive
    if parts[0] == "END":
        break

    # Check for a label (symbol)
    if parts[0] not in keywords:
        label = parts[0]
        symbol_table[label] = loc_counter  # Assign current LC to label

        # Handle DS (Define Storage)
        if len(parts) > 1 and parts[1] == "DS":
            loc_counter += int(parts[2])
        else:
            loc_counter += 1
    else:
        loc_counter += 1  # Instruction without label

# Output: Print the Symbol Table
print("Symbol Table:")
print("{:<10} {:<10}".format("Symbol", "Address"))
for symbol, address in symbol_table.items():
    print("{:<10} {:<10}".format(symbol, address))