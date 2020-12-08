# Day 7: uh oh
import re
import pprint


def build_rules(file):
    raw = file.readlines()

    # construct a dict. First, a rough pass that splits the first color from
    # the stuff it contains
    ruledict = {}
    for line in raw:
        color, contents = line.split("bags contain ")
        ruledict[color] = contents

    # now, via judicious use of regex, split the contents string into a list
    regex = " bags?[,.]? *"
    for color in ruledict:
        # the last item in the list is always just "\n" so throw it out
        ruledict[color] = re.split(regex, ruledict[color].strip())[:-1]

    return ruledict


def main():
    with open("input/day7.txt") as f:
        rules = build_rules(f)
    pprint.pprint(rules)


if __name__ == '__main__':
    main()
