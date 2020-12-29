# day 18: ugh, an algebra
# evaluate the expressions but with different than normal operator precedence
# addition and multiplication at the same level, evaluated left to right
# parentheses take precedence over + or *, as usual

import re


def parser(input):
    ans = 0
    temp = 0
    nextop = "+"
    inputlist = input.split()
    for elem in inputlist:
        if elem == "*":
            nextop = "*"
        elif elem == "+":
            nextop = "+"
        else:
            temp = int(elem)
            if nextop == "*":
                ans *= temp
            elif nextop == "+":
                ans += temp
    return ans


def crawl(input, part2):
    parens = re.search("(\\([^\\(\\)]*\\))", input)
    if parens is None:
        if part2:
            return parser(addfirst(input))
        else:
            return parser(input)
    else:
        parenblob = parens.group()[1:-1]
        if part2:
            intermed = parser(addfirst(parenblob))
        else:
            intermed = parser(parenblob)
        intermed_input = input[0:parens.start()] + str(intermed) + \
            input[parens.end():]
        return crawl(intermed_input, part2)


def addfirst(input):
    inlist = input.split()

    while "+" in inlist:
        p = inlist.index("+") - 1
        a, plus, b = int(inlist.pop(p)), inlist.pop(p), int(inlist.pop(p))
        inlist.insert(p, str(a + b))

    return " ".join(inlist)


def main():
    with open("input/day18.txt") as f:
        input = f.readlines()
    # input = ["2 * 3 + (4 * 5)",
    #          "5 + (8 * 3 + 9 + 3 * 4 * 3)",
    #          "5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))",
    #          "((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"]
    total = 0
    for i in input:
        total += crawl(i, False)
    print("Part 1:", total)

    # part 2...do additions first and then multiplications. opposite operator
    # precedence from normal...
    # input = ["2 * 3 + (4 * 5)",
    #          "5 + (8 * 3 + 9 + 3 * 4 * 3)",
    #          "5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))",
    #          "((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"]
    total = 0
    for i in input:
        # print(crawl(i, True))
        total += crawl(i, True)
    print("Part 2:", total)


if __name__ == '__main__':
    main()
