import re


def is_passport_valid_part1(passport):
    passport_dict = {}
    for string in passport:
        split = string.split(':')
        key = split[0]
        value = split[1]
        passport_dict.setdefault(key, value)

    return required_fields_in(passport_dict)


def required_fields_in(passport_dict) -> bool:
    return 'byr' in passport_dict and 'iyr' in passport_dict and 'eyr' in passport_dict and \
           'hgt' in passport_dict and 'hcl' in passport_dict and 'ecl' in passport_dict and \
           'pid' in passport_dict


# TODO: giving a result that's too high
def is_passport_valid_part2(passport):
    passport_dict = {}
    for string in passport:
        split = string.split(':')
        key = split[0]
        value = split[1]

        if key == 'byr':
            birth_year = int(value)
            if len(value) != 4 or birth_year < 1920 or birth_year > 2002:
                return False
        elif key == 'iyr':
            issue_year = int(value)
            if len(value) != 4 or issue_year < 2010 or issue_year > 2020:
                return False
        elif key == 'eyr':
            exp_year = int(value)
            if len(value) != 4 or exp_year < 2020 or exp_year > 2030:
                return False
        elif key == 'hgt':
            unit = value[-2:]
            if not str.isdigit(value[:-2]):
                return False
            height = int(value[:-2])

            # assumption is unit has to be either cm or in
            if unit == 'cm':
                if height < 150 or height > 193:
                    return False
            elif unit == 'in':
                if height < 59 or height > 76:
                    return False
        elif key == 'hcl':
            regex = re.compile(r'#[a-f0-9]{6}')
            if regex.match(value) is None:
                return False
        elif key == 'ecl':
            if value not in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}:
                return False
        elif key == 'pid':
            if len(value) != 9 or not str.isdigit(value):
                return False

        passport_dict.setdefault(key, value)

    return required_fields_in(passport_dict)


def count_valid_passports(lines: [str], is_passport_valid) -> int:
    # end of the file newline
    lines.append('\n')

    passport = []
    num_valid = 0
    for line in lines:
        if line != '\n':
            passport = passport + line.strip().split(' ')

        # don't want to use an else here intentionally
        if line == '\n':
            if is_passport_valid(passport):
                num_valid = num_valid + 1
            # reset
            passport = []

    return num_valid


if __name__ == '__main__':
    with open('day4input.txt', 'r') as file:
        batch = file.readlines()
        # print('Part 1:', count_valid_passports(batch, is_passport_valid_part1))
        print('Part 2:', count_valid_passports(batch, is_passport_valid_part2))
