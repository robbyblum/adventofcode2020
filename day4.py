# Day 4. Part 1: count valid passports.
# There are 8 possible passport fields:
# byr (Birth Year)
# iyr (Issue Year)
# eyr (Expiration Year)
# hgt (Height)
# hcl (Hair Color)
# ecl (Eye Color)
# pid (Passport ID)
# cid (Country ID)
# Valid passports must have all of these fields except cid, which is optional
# fields are key:value and separated by space or newline
# passport entries are separated by blank lines


def parse_passports(file):
    # i see how this could be done with a highly cursed one-liner,
    # and i choose not to do so
    raw = file.read()
    plist = [p.split() for p in raw.split("\n\n")]
    pdict = [dict(field.split(":") for field in p) for p in plist]
    return pdict


def check_passport(passport):
    # not checking for cid right now
    valid = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    return all(field in passport for field in valid)


def main():
    with open("input/day4.txt") as f:
        passports = parse_passports(f)

    # part 1
    numvalid = 0
    for passport in passports:
        if check_passport(passport):
            numvalid += 1

    print("Part 1:", numvalid, "out of", len(passports))


if __name__ == '__main__':
    main()
