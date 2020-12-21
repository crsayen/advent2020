rules = []
with open('input7') as f:
    for line in f:
        rules.append(line.replace('\n', ''))

bags = {}

for rule in rules:
    subject, contents = rule.split(' contain ')
    adj, color, _bag = subject.split(' ')
    subject = adj + color
    bags[subject] = []
    contents = contents.replace('.', '')
    contentsList = contents.split(',')
    for content in contentsList:
        if content == 'no other bags':
            continue
        if content[0] == ' ': content = content[1:]
        _num, adj, color, _bag = content.split(' ')
        bags[subject].append(adj + color)

def fill(bagList):
    if len(bagList) == 0: return bagList
    thisout = []
    for bag in bagList:
        _contents = bags[bag]
        thisout = bagList + thisout + _contents + fill(_contents)
    return thisout

out = {}

for bag in bags.keys():
    out[bag] = fill(bags[bag])

count = 0

for shit in out:
    if 'shinygold' in out[shit]:
        count += 1

print(count)