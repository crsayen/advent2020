instructions = []
with open('input8') as f:
    for line in f:
        line = line.replace('\n', '')
        op, value = line.split(' ')
        instructions.append({"op": op, 'value': int(value)})



def attempt(instructions):
    accumulator = 0
    visited = []
    pcounter = 0
    while pcounter != len(instructions):
        if pcounter in visited: return None
        visited.append(pcounter)
        instruction = instructions[pcounter]
        if instruction['op'] == 'acc':
            accumulator += instruction['value']
            pcounter += 1
        elif instruction['op'] == 'jmp':
            pcounter += instruction['value']
        elif instruction['op'] == 'nop':
            pcounter += 1
    return accumulator

for i, instruction in enumerate(instructions):
    if instruction['op'] == 'jmp':
        newInstruction = {'op': 'nop'}
        result = attempt([*instructions[:i], newInstruction, *instructions[i + 1:]])
        if result is not None:
            print(result)
    elif instruction['op'] == 'nop':
        newInstruction = {'op': 'jmp', 'value': instruction['value']}
        result = attempt([*instructions[:i], newInstruction, *instructions[i + 1:]])
        if result is not None:
            print(result)
