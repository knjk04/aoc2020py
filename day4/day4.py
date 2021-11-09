def is_passport_valid(passport):
    passport_dict = {}
    for string in passport:
        split = string.split(':')
        key = split[0]
        value = split[1]
        passport_dict.setdefault(key, value)

    return 'byr' in passport_dict and 'iyr' in passport_dict and 'eyr' in passport_dict and \
           'hgt' in passport_dict and 'hcl' in passport_dict and 'ecl' in passport_dict and \
           'pid' in passport_dict


def count_valid_passports(lines: [str]) -> int:
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
        print(count_valid_passports(batch))
