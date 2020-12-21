expenses = None
with open('input1') as f:
    expenses = [int(line) for line in f]

for expense1 in expenses:
    for expense2 in expenses:
        for expense3 in expenses:
            if expense1 + expense2 + expense3 == 2020:
                print(expense1 * expense2 * expense3)