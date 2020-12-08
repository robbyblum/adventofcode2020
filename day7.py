# Day 7: uh oh
import re
import pprint


def build_rules(file):
    raw = file.readlines()

    # construct a dict. First, a rough pass that splits the first color from
    # the stuff it contains
    ruledict = {}
    for line in raw:
        color, contents = line.split(" bags contain ")
        ruledict[color] = contents

    # now, via judicious use of regex, split the contents string into a list
    regex = " bags?[,.]? *"
    for color in ruledict:
        # the last item in the list is always just "\n" so throw it out
        contents = re.split(regex, ruledict[color].strip())[:-1]
        # actually let's prep for part 2, because i expect to need the numbers
        # for it. Let's make contents another dict actually
        if contents == ['no other']:
            ruledict[color] = {'no other': 0}  # sure why not
        else:
            ruledict[color] = {color2: num for (num, color2) in (
                s.split(maxsplit=1) for s in contents)}

    return ruledict


def main():
    with open("input/day7.txt") as f:
        rules = build_rules(f)

    # temp = {}
    # for rule in rules:
    #     if "salmon" in rule:
    #         temp[rule] = rules[rule]
    # pprint.pprint(temp)

    mybag = 'shiny gold'
    bagqueue = [mybag]
    output1 = []
    while len(bagqueue) > 0:
        testbag = bagqueue.pop()
        for color in rules:
            if testbag in rules[color]:
                output1.append(color)
                bagqueue.append(color)
                # print(f"{color}!")

    # remove duplicates by just doing set() at the end, screw it
    print("Part 1:", len(set(output1)))

    return output1


if __name__ == '__main__':
    main()
