total = 0
with open('input6') as f:
    group = []
    for line in f:
        group = (group + [c if c in 'abcxyz' else '' for c in line])
        if line == '\n':
            total += len(set(group))
            group = []
    total += len(set(group))
        

print(total)