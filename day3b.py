m = None
slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]

total = 1

for slope in slopes:
    with open("input3") as f:
        position = 0
        count = 0
        skip = slope[1]
        for i, line in enumerate(f):
            if i == 0 or i % skip != 0:
                continue
            position = (position + slope[0]) % (len(line) - 1)
            if line[position] == "#":
                count += 1
        print(count)
    total *= count

print(total)
