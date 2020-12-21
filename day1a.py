expenses = None
with open('input1') as f:
    expenses = [int(line) for line in f]

for expense1 in expenses:
    for expense2 in expenses:
        if expense1 + expense2 == 2020:
            print(expense1 * expense2)