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
            ruledict[color] = {color2: int(num) for (num, color2) in (
                s.split(maxsplit=1) for s in contents)}

    return ruledict


# this does the recursive bag-counting for part 2
def countbags(color, bagdict):
    if color in bagdict:
        subdict = bagdict[color]
        m = 0
        for subcolor in subdict:
            n = subdict[subcolor]
            m += n + n * countbags(subcolor, bagdict)
        return m
    else:
        return 0


def main():
    with open("input/day7.txt") as f:
        rules = build_rules(f)

    # temp = {}
    # for rule in rules:
    #     if "salmon" in rule:
    #         temp[rule] = rules[rule]
    # pprint.pprint(temp)

    # part 1:
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

    # return output1

    # part 2
    # actually don't need any of this part
    # # First let's walk *down* from the shiny gold bag, to get the
    # # list of colors we need to add up
    # bagqueue = [mybag]
    # output2 = []
    # while len(bagqueue) > 0:
    #     # i guess this is depth first, instead of breadth first?
    #     testbag = bagqueue.pop()
    #     for color in rules[testbag]:
    #         if color != 'no other':
    #             output2.append(color)
    #             bagqueue.append(color)
    #             print(f"in {testbag}: {color}!")
    #         else:
    #             print(f"in {testbag}: nothing!")
    # print(len(output2))
    # all I need is this!
    print("Part 2:", countbags('shiny gold', rules))


if __name__ == '__main__':
    main()
