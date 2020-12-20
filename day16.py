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


def load_file(path):
    # load the data in three chunks
    with open(path) as f:
        raw = f.read()
    raw_rules, raw_mytix, raw_neartix = raw.split("\n\n")

    # parse and format the data
    ruleslist = raw_rules.splitlines()
    rules = parse_rules(ruleslist)

    mytix = raw_mytix.splitlines()[1].split(',')

    neartix = [t.split(',') for t in raw_neartix.splitlines()[1:]]
    return rules, mytix, neartix


def parse_rules(ruleslist):
    """parse a list of rules into a dict of rules"""
    return ruleslist


def main():
    rules, mytix, neartix = load_file("input/day16.txt")
    print(rules)
    print(mytix)
    # print(neartix)


if __name__ == '__main__':
    main()
