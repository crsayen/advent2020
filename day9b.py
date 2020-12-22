inp = None
with open('input9') as f:
    inp = [int(line.replace('\n', '')) for line in f]

goal = 756008079
goalIndex = inp.index(goal)

for ln in range(1, goalIndex + 1):
    for start in range(0, goalIndex + 1 - ln):
        subArr = inp[start: start + ln]
        if sum(subArr) == goal:
            print(subArr)
            print(max(subArr) + min(subArr))
