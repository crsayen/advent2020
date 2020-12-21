total = 0
bigstr = ''
with open('input6') as f:
    for line in f:
        bigstr += line

groups = bigstr.split('\n\n')

for group in groups:
    total += len(set([c for c in group.replace('\n', '')]))
        

print(total)