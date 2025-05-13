#que 7
# Assembly code lines
assembly_code = [
    "START 300",
    "READ M",
    "MOVER AREG, ='11'",
    "MOVEM AREG, N",
    "MOVER BREG, ='61'",
    "ADD AREG, BREG",
    "COMP AREG, M",
    "BC GT, LAST",
    "LTORG",
    "NEXT SUB AREG, ='11'",
    "MOVER CREG, N",
    "ADD CREG, ='81'",
    "MOVEM CREG, N",
    "PRINT Y",
    "LAST STOP",
    "M DS 1",
    "N DS 1",
    "END"
]

# Initialize tables and location counter
literal_table = []
pool_table = []
loc_counter = 0
literals = []

# Pass 1: Process the code and handle literals
for line in assembly_code:
    parts = line.strip().split()

    if not parts:
        continue

    # START directive
    if parts[0] == "START":
        loc_counter = int(parts[1])
        continue

    # Scan for literals (always allow duplicates)
    for part in parts:
        if part.startswith("='"):
            literals.append(part)

    # LTORG or END assigns addresses to literals
    if parts[0] in ["LTORG", "END"]:
        if literals:
            pool_table.append(len(literal_table) + 1)  # 1-based indexing
            for lit in literals:
                literal_table.append({
                    'literal': lit,
                    'address': loc_counter
                })
                loc_counter += 1
            literals = []

    # Handle DS declarations
    elif len(parts) > 1 and parts[1] == "DS":
        loc_counter+=int(parts[2])
    else:
        loc_counter += 1

# Output the Literal Table
print("\nLiteral Table:")
print("{:<10} {:<10}".format("Literal", "Address"))
for item in literal_table:
    print("{:<10} {:<10}".format(item['literal'], item['address']))

# Output the Pool Table
print("\nPool Table:")
print("{:<15}".format("Pool Start Index"))
for index in pool_table:
    print("{:<15}".format(index))
