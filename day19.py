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

# inp = """42: 9 14 | 10 1
# 9: 14 27 | 1 26
# 10: 23 14 | 28 1
# 1: "a"
# 11: 42 31
# 5: 1 14 | 15 1
# 19: 14 1 | 14 14
# 12: 24 14 | 19 1
# 16: 15 1 | 14 14
# 31: 14 17 | 1 13
# 6: 14 14 | 1 14
# 2: 1 24 | 14 4
# 0: 8 11
# 13: 14 3 | 1 12
# 15: 1 | 14
# 17: 14 2 | 1 7
# 23: 25 1 | 22 14
# 28: 16 1
# 4: 1 1
# 20: 14 14 | 1 15
# 3: 5 14 | 16 1
# 27: 1 6 | 14 18
# 14: "b"
# 21: 14 1 | 1 14
# 25: 1 1 | 1 14
# 22: 14 14
# 8: 42
# 26: 14 22 | 1 20
# 18: 15 15
# 7: 14 5 | 1 21
# 24: 14 1
#
# abbbbbabbbaaaababbaabbbbabababbbabbbbbbabaaaa
# bbabbbbaabaabba
# babbbbaabbbbbabbbbbbaabaaabaaa
# aaabbbbbbaaaabaababaabababbabaaabbababababaaa
# bbbbbbbaaaabbbbaaabbabaaa
# bbbababbbbaaaaaaaabbababaaababaabab
# ababaaaaaabaaab
# ababaaaaabbbaba
# baabbaaaabbaaaababbaababb
# abbbbabbbbaaaababbbbbbaaaababb
# aaaaabbaabaaaaababaa
# aaaabbaaaabbaaa
# aaaabbaabbaaaaaaabbbabbbaaabbaabaaa
# babaaabbbaaabaababbaabababaaab
# aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba""".split('\n\n')


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
newrule21 = '(' + expandrules(rules, 42) + '){2}(' + expandrules(rules, 31) + '){1}'
newrule31 = '(' + expandrules(rules, 42) + '){3}(' + expandrules(rules, 31) + '){1,2}'
newrule41 = '(' + expandrules(rules, 42) + '){4}(' + expandrules(rules, 31) + '){1,3}'
newrule51 = '(' + expandrules(rules, 42) + '){5}(' + expandrules(rules, 31) + '){1,4}'
newrule61 = '(' + expandrules(rules, 42) + '){6}(' + expandrules(rules, 31) + '){1,5}'
newrule71 = '(' + expandrules(rules, 42) + '){7}(' + expandrules(rules, 31) + '){1,6}'

def countvalid(rule, input):
    n = 0
    for i in input:
        if re.fullmatch(rule, i):
            n += 1
    return n


# print(countvalid(newrule21, inputs))
# print(countvalid(newrule31, inputs))
# print(countvalid(newrule41, inputs))
# print(countvalid(newrule51, inputs))
# print(countvalid(newrule61, inputs))
# print(countvalid(newrule71, inputs))
total = 0
newrules = [newrule21, newrule31, newrule41, newrule51, newrule61, newrule71]
for nr in newrules:
    total += countvalid(nr, inputs)

print("Part 2:", total)
