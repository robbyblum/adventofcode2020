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
            # outrule += '(' + expandrules(ruledict, int(ch)) + ')'
            subrule = expandrules(ruledict, int(ch))
            if '|' in subrule:
                outrule += '(' + subrule + ')'
            else:
                outrule += subrule
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

# part 2: replace two rules (8 and 11) with the following:
"""
8: 42 | 42 8
11: 42 31 | 42 11 31
"""
# now it contains loops. wonderful. Also, rule 0 is "8 11" so these are pretty
# high up the list of things...
# what this really means, tbh, is "42 M times, then 31 N times, where M > N"
# (and N >= 1).

def countvalid(rule, input):
    n = 0
    for i in input:
        if re.fullmatch(rule, i):
            n += 1
    return n

rule42 = '(' + expandrules(rules, 42) + ')'
rule31 = '(' + expandrules(rules, 31) + ')'
total = 0
n = 1
while True:
    nr = f'{rule42}{{{n+1}}}{rule31}{{1,{n}}}'
    total += countvalid(nr, inputs)
    if countvalid(nr, inputs) == 0:
        print(n)
        break
    else:
        n += 1

print("Part 2:", total)
