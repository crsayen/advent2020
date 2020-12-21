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
        num, adj, color, _bag = content.split(' ')
        for _ in range(int(num)):
            bags[subject].append(adj + color)

count = 0

def countContents(bagName):
    global count
    _contents = bags[bagName]
    for bag in _contents:
        count += 1
        countContents(bag)

countContents('shinygold')

print(count)