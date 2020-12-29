# day 19. this feels like regex hell, we'll see
# actually the regex wasn't very hard. it's quite long, but it works,
# and was very straightforward to build!
import re
import collections

# inp = """0: 4 1 5
# 1: 2 3 | 3 2
# 3: 4 5 | 5 4
# 2: 4 4 | 5 5
# 4: "a"
# 5: "b"
#
# ababbb
# bababa
# abbbab
# aaabbb
# aaaabbb""".split("\n\n")
with open("input/day19.txt") as f:
    inp = f.read().split("\n\n")


def expandrules(ruledict, startid):
    inrule = ruledict[startid].split()
    outrule = ''
    for ch in inrule:
        if ch == 'a' or ch == 'b' or ch == '|':
            outrule += ch
        else:
            outrule += '(' + expandrules(ruledict, int(ch)) + ')'
    return outrule


rulesraw = inp[0].splitlines()
inputs = inp[1].splitlines()
rules = collections.defaultdict(str)
for line in rulesraw:
    i, rulestr = line.split(": ")
    # simplify the strings; remove quotes
    rules[int(i)] = rulestr.replace('"', '')
# print(rules)
# print(expandrules(rules, 0))

numvalid = 0
for i in inputs:
    if re.fullmatch(expandrules(rules, 0), i):
        numvalid += 1
print("Part 1:", numvalid)
