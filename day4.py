# Day 4. Part 1: count valid passports.
# There are 8 possible passport fields:

# byr (Birth Year) - four digits; at least 1920 and at most 2002.
# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
# hgt (Height) - a number followed by either cm or in:
#     If cm, the number must be at least 150 and at most 193.
#     If in, the number must be at least 59 and at most 76.
# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
# pid (Passport ID) - a nine-digit number, including leading zeroes.
# cid (Country ID) - ignored, missing or not.

# Valid passports must have all of these fields except cid, which is optional
# fields are key:value and separated by space or newline
# passport entries are separated by blank lines


# parse passports from input file
def parse_passports(file):
    # i see how this could be done with a highly cursed one-liner,
    # and i choose not to do so
    raw = file.read()
    plist = [p.split() for p in raw.split("\n\n")]
    pdict = [dict(field.split(":") for field in p) for p in plist]
    return pdict


# check for the presence of the required fields
def check_passport_fields(passport):
    # not checking for cid right now
    valid = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    return all(field in passport for field in valid)


# validate fields according to their rules
def validate_field(passport, field):
    import re

    instring = passport[field]

    if field == 'byr':
        # byr (Birth Year) - four digits; at least 1920 and at most 2002.
        year = int(instring)
        return (year >= 1920) and (year <= 2002)

    elif field == 'iyr':
        # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
        year = int(instring)
        return (year >= 2010) and (year <= 2020)

    elif field == 'eyr':
        # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
        year = int(instring)
        return (year >= 2020) and (year <= 2030)

    elif field == 'hgt':
        # hgt (Height) - a number followed by either cm or in:
        #     If cm, the number must be at least 150 and at most 193.
        #     If in, the number must be at least 59 and at most 76.
        try:
            height = int(instring[:-2])
            unit = instring[-2:]
            if unit == 'in':
                return (height >= 59) and (height <= 76)
            elif unit == 'cm':
                return (height >= 150) and (height <= 193)
            else:
                return False
        except Exception as e:
            return False

    elif field == 'hcl':
        # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
        pattern = '#[0-9a-f]{6}'
        return bool(re.fullmatch(pattern, instring))

    elif field == 'ecl':
        # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
        valid_eye = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        return instring in valid_eye

    elif field == 'pid':
        # pid (Passport ID) - a nine-digit number, including leading zeroes.
        pattern = '[0-9]{9}'
        return bool(re.fullmatch(pattern, instring))

    else:
        print("Error: invalid field")
        return False  # probably wrong way to handle this, w/e


def main():
    with open("input/day4.txt") as f:
        passports = parse_passports(f)

    valid = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    # gonna do part 1 and part 2 in the same loop, why not
    numvalid_p1 = 0
    numvalid_p2 = 0
    for passport in passports:
        if check_passport_fields(passport):
            numvalid_p1 += 1
            if all(validate_field(passport, field) for field in valid):
                numvalid_p2 += 1

    print("Part 1:", numvalid_p1, "out of", len(passports))
    print("Part 2:", numvalid_p2, "out of", len(passports))


if __name__ == '__main__':
    main()
