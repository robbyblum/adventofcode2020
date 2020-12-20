# day 16...train tickets? Example ticket:

# .--------------------------------------------------------.
# | ????: 101    ?????: 102   ??????????: 103     ???: 104 |
# |                                                        |
# | ??: 301  ??: 302             ???????: 303      ??????? |
# | ??: 401  ??: 402           ???? ????: 403    ????????? |
# '--------------------------------------------------------'

# Start by determining which tickets are completely invalid; these are tickets
# that contain values which aren't valid for any field. Ignore your ticket for
# now. For example, suppose you have the following notes:

# class: 1-3 or 5-7
# row: 6-11 or 33-44
# seat: 13-40 or 45-50
#
# your ticket:
# 7,1,14
#
# nearby tickets:
# 7,3,47
# 40,4,50
# 55,2,20
# 38,6,12

# It doesn't matter which position corresponds to which field; you can identify
# invalid nearby tickets by considering only whether tickets contain values
# that are not valid for any field. In this example, the values on the first
# nearby ticket are all valid for at least one field. This is not true of the
# other three nearby tickets: the values 4, 55, and 12 are are not valid for
# any field. Adding together all of the invalid values produces your ticket
# scanning error rate: 4 + 55 + 12 = 71.

# Consider the validity of the nearby tickets you scanned. What is
# your ticket scanning error rate?
import re
from pprint import pprint


def load_input(path):
    # load the data in three chunks
    with open(path) as f:
        raw = f.read()
    raw_rules, raw_mytix, raw_neartix = raw.split("\n\n")

    # parse and format the data
    ruleslist = raw_rules.splitlines()
    rules = parse_rules(ruleslist)

    mytix = [int(n) for n in raw_mytix.splitlines()[1].split(',')]

    # surely there's a better way to do this, that I'm not remembering...
    raw_neartix = [t.split(',') for t in raw_neartix.splitlines()[1:]]
    neartix = []
    for tix in raw_neartix:
        neartix.append([int(n) for n in tix])

    return rules, mytix, neartix


def parse_rules(ruleslist):
    """parse a list of rules into a dict of rules"""
    rules = {}
    for r in ruleslist:
        key, low1, hi1, low2, hi2 = re.split(": |-| or ", r)
        rules[key] = [(int(low1), int(hi1)), (int(low2), int(hi2))]
    return rules


def inrange(number, range):
    """convenience function. is number inside range? range is tuple (low, hi),
    checks range inclusive of the endpoints"""
    return (number >= range[0] and number <= range[1])


def main():
    rules, mytix, neartix = load_input("input/day16.txt")
    fields = list(rules.keys())

    # PART 1:
    # I suppose I could merge the valid ranges and check fewer things...or I
    # could just not do that. I'm going to just not do that.
    invalid = []
    for tix in neartix:
        for n in tix:
            for rule in rules.values():
                if inrange(n, rule[0]) or inrange(n, rule[1]):
                    # if we find a valid rule, move on to the next number
                    break
            # if we exhausted the list without finding a valid rule, it's
            # an invalid number
            else:
                invalid.append(n)
    # invalid.sort()
    # print(invalid)
    # print(len(invalid), len(set(invalid)))
    print("Part 1:", sum(invalid))

    # PART 2:
    # oops I should have been tracking which tickets were invalid. Go back and
    # do that now...
    validtix = []
    for tix in neartix:
        if not any(n in invalid for n in tix):
            validtix.append(tix)

    # for each rule, find all positions that *could* correspond to that rule
    validrules = {key: [] for key in fields}
    for i in range(len(mytix)):
        near_n = [t[i] for t in validtix]
        for field in fields:
            r1, r2 = rules[field][0:2]
            if all((inrange(n, r1) or inrange(n, r2)) for n in near_n):
                validrules[field].append(i)

    # print(validrules)

    # Now I want to assume that one of these only has 1 valid possibility.
    # This happens to be 'class': [3] for me. Start there, assign position 3
    # to the 'class' rule, and remove 3 from all the other lists for other
    # rules. Then go to the next shortest list of valid locations, and repeat.
    lengths = [len(v) for v in (validrules[f] for f in fields)]
    fields_sort = [x for _, x in sorted(zip(lengths, fields),
                                        key=lambda pair: pair[0])]
    # print(fields_sort)
    rules_assign = {}
    while len(fields_sort) > 0:
        fs = fields_sort.pop(0)
        pos = validrules.pop(fs)[0]
        rules_assign[fs] = pos
        for rule in validrules:
            validrules[rule].remove(pos)
    print("{field: position}:", rules_assign)

    mydepfields = []
    depfields = ['departure location', 'departure station',
                 'departure platform', 'departure track',
                 'departure date', 'departure time']
    for fs in depfields:
        pos = rules_assign[fs]
        mydepfields.append(mytix[pos])
    print(mydepfields)
    prod = 1
    for n in mydepfields:
        prod *= n
    print("Part 2:", prod)


if __name__ == '__main__':
    main()
