def isSum(number, preamble):
    arr = [n for n in preamble if n < number]
    for i, a in enumerate(arr):
        for j, b in enumerate(arr):
            if i == j: continue
            if a + b == number: return True
    return False

inp = None
with open('input9') as f:
    inp = [int(line.replace('\n', '')) for line in f]

ln = len(inp)

for i in range(25, ln):
    number = inp[i]
    preamble = inp[i - 25: i]
    if not isSum(number, preamble):
        print(inp[i])

