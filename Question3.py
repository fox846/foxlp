#Que 3
# Updated Assembly code lines (as per your input)
assembly_code = [
    "START 180",
    "READ M",
    "READ N",
    "LOOP	MOVER AREG, M",
	        "MOVER BREG, N",
          "COMP BREG, =’200’",
	        "BC GT, LOOP",
    "BACK SUB AREG, M",
          "COMP AREG, =’500’",
	        "BC LT, BACK",
     "STOP",
     "M	  DS	1",
     "N	  DS	1",
	   "END"

]

# Initialize symbol table and location counter
symbol_table = {}
loc_counter = 0

# Define instruction keywords (to avoid confusing with labels)
keywords = ["START", "END", "READ", "MOVER", "COMP", "BC", "STOP", "DS"]

# Pass 1: Build Symbol Table
for line in assembly_code:
    parts = line.strip().split()

    if not parts:
        continue

    # START directive
    if parts[0] == "START":
        loc_counter = int(parts[1])
        continue

    # END directive
    if parts[0] == "END":
        break

    # If label exists
    if parts[0] not in keywords:
        label = parts[0]
        symbol_table[label] = loc_counter

        # If it’s a storage declaration (DS)
        if len(parts) > 1 and parts[1] == "DS":
            loc_counter += int(parts[2])
        else:
            loc_counter += 1
    else:
        loc_counter += 1

# Output the symbol table
print("Symbol Table:")
print("{:<10} {:<10}".format("Symbol", "Address"))
for symbol, address in symbol_table.items():
    print("{:<10} {:<10}".format(symbol, address))