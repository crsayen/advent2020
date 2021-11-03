inp = None
with open('input16') as f:
    inp = f.read()

rules, rest = inp.split('your ticket:')
myTicket_str, nearbyTickets_str = rest.split('nearby tickets:')


def csl2tickets(text: str):
    return [[int(n) for n in l.split(',') if not n in ["", ","]]
            for l in text.split('\n') if l != ""]


class Rule:
    def __init__(self, rule):
        self.name, ranges = rule.split(': ')
        sr1, sr2 = ranges.split(' or ')
        self.r1 = [int(s) for s in sr1.split('-')]
        self.r1[1] += 1
        self.r2 = [int(s) for s in sr2.split('-')]
        self.r2[1] += 1

    def check(self, n):
        return (n in range(*self.r1) or n in range(*self.r2))


[my_t] = csl2tickets(myTicket_str)
n_ts = csl2tickets(nearbyTickets_str)


error_rate = 0
checkers = [Rule(rstr) for rstr in rules.split('\n') if rstr != ""]
for t in [i for l in n_ts for i in l]:
    passes = [True for checker in checkers if checker.check(t)]
    if not len(passes):
        error_rate += t
print(error_rate)
