instructions = []
with open('input8') as f:
    for line in f:
        line = line.replace('\n', '')
        op, value = line.split(' ')
        instructions.append({"op": op, 'value': int(value)})

accumulator = 0

visited = []

pcounter = 0

while True:
    if pcounter in visited: break
    visited.append(pcounter)
    instruction = instructions[pcounter]
    if instruction['op'] == 'acc':
        accumulator += instruction['value']
        pcounter += 1
    elif instruction['op'] == 'jmp':
        pcounter += instruction['value']
    elif instruction['op'] == 'nop':
        pcounter += 1

print(accumulator)
