# Opcode and register tables
opcode_table = {
    'START': ('AD', 1),
    'END': ('AD', 2),
    'READ': ('IS', 9),
    'MOVER': ('IS', 4),
    'SUB': ('IS', 2),
    'STOP': ('IS', 0),
    'DS': ('DL', 1)
}

register_table = {
    'AREG': 1
}

# Input assembly code
assembly_code = [
    "START 100",
    "READ A",
    "READ B",
    "MOVER AREG, A",
    "SUB AREG, B",
    "STOP",
    "A DS 1",
    "B DS 1",
    "END"
]

# Pass 1: Generate symbol table and intermediate code
symbol_table = {}
location_counter = 0
intermediate_code = []

for line in assembly_code:
    parts = line.strip().split()

    if not parts:
        continue

    if parts[0] == 'START':
        location_counter = int(parts[1])
        intermediate_code.append((location_counter, 'AD', 1, parts[1]))

    elif parts[0] == 'END':
        intermediate_code.append((location_counter, 'AD', 2, ''))
        break

    elif parts[0] == 'READ':
        symbol = parts[1]
        intermediate_code.append((location_counter, 'IS', 9, symbol))
        location_counter += 1

    elif parts[0] in ['MOVER', 'SUB']:
        opcode = parts[0]
        reg, mem = parts[1].split(',')[0], parts[1].split(',')[1]
        reg_code = register_table[reg]
        intermediate_code.append((location_counter, 'IS', opcode_table[opcode][1], reg_code, mem))
        location_counter += 1

    elif parts[0] == 'STOP':
        intermediate_code.append((location_counter, 'IS', 0, ''))
        location_counter += 1

    elif parts[1] == 'DS':
        symbol_table[parts[0]] = location_counter
        intermediate_code.append((location_counter, 'DL', 1, parts[2]))
        location_counter += 1

# Pass 2: Replace symbols with addresses
final_intermediate_code = []

for entry in intermediate_code:
    final_entry = []
    for item in entry:
        if isinstance(item, str) and item in symbol_table:
            final_entry.append(symbol_table[item])
        else:
            final_entry.append(item)
    final_intermediate_code.append(tuple(final_entry))

# Output Symbol Table
print("Symbol Table:")
for symbol, addr in symbol_table.items():
    print(f"{symbol} -> {addr}")

# Output Intermediate Code
print("\nIntermediate Code:")
for line in final_intermediate_code:
    print(line)