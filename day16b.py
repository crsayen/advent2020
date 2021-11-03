from math import prod
import sys
inp = None
with open('input16') as f:
    inp = f.read()


def csl2tickets(text: str):
    return [[int(n) for n in l.split(',') if not n in ["", ","]]
            for l in text.split('\n') if l != ""]


class Rule:
    def __init__(self, rule_str: str):
        self.name, self.rangestr = rule_str.split(': ')
        sr1, sr2 = self.rangestr.split(' or ')
        self.r1 = [int(s) for s in sr1.split('-')]
        self.r1[1] += 1
        self.r2 = [int(s) for s in sr2.split('-')]
        self.r2[1] += 1

    def check(self, n: int) -> bool:
        return (n in range(*self.r1) or n in range(*self.r2))


def getRules(rule_str: str):
    return [Rule(rstr) for rstr in rule_str.split('\n') if rstr != ""]


def getValidTickets(tickets, rules: "list[Rule]"):
    return [t for t in tickets if all(
        [len([True for rule in rules if rule.check(f)]) for f in t]
    )]


def getValidFieldPositions(rule, tickets) -> "list[int]":
    return [fi for fi in range(len(tickets[0])) if all([
        rule.check(f) for f in [t[fi] for t in tickets]])]


def getFieldPosition(field_pos: "list[int]", other_field_pos: "list[list[int]]") -> int:
    return [p for p in field_pos if p not in [op for of in other_field_pos for op in of]][0]


rule_str, rest = inp.split('your ticket:')
myTicket_str, nearbyTickets_str = rest.split('nearby tickets:')

rules = getRules(rule_str)
[my_t] = csl2tickets(myTicket_str)
v_ts = getValidTickets(csl2tickets(nearbyTickets_str), rules)
print(len(v_ts))

field_positions: "dict[str, list[int]]" = {
    r.name: getValidFieldPositions(r, v_ts) for r in rules}

field_map: "dict[str, int]" = {
    n: getFieldPosition(
        f,
        [of for (on, of) in field_positions.items() if on != n]
    ) for (n, f) in field_positions.items()
}

print(151 * 113 * 113 * 151 * 151 * 151)

print(prod([my_t[fi]
            for (fn, fi) in field_map.items() if fn.startswith('departure')]))
