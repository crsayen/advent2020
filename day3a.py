m = None

with open("input3") as f:
    position = 0
    count = 0
    for i, line in enumerate(f):
        if not i:
            continue
        position = (position + 3) % (len(line) - 1)
        if line[position] == "#":
            count += 1

print(count)
