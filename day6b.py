total = 0
bigstr = ''
with open('input6') as f:
    for line in f:
        bigstr += line

groups = bigstr.split('\n\n')

for group in groups:
    allAnswers = set([c for c in group.replace('\n', '')])
    individualAnswers = group.split('\n')
    for answer in allAnswers:
        allAnswered = True
        for individualsAnswers in individualAnswers:
            if answer not in individualsAnswers:
                allAnswered = False
                break
        if allAnswered: total += 1
        

print(total)