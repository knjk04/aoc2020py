def count_valid_passwords_part1(lines: [str]) -> int:
    valid = 0
    for line in lines:
        split = line.split(' ')
        occurrences = split[0].split('-')

        min_times = int(occurrences[0])
        max_times = int(occurrences[1])
        letter = (split[1])[0]
        password = split[-1]

        count = password.count(letter)
        if min_times <= count <= max_times:
            valid = valid + 1
    return valid


def count_valid_passwords_part2(lines: [str]) -> int:
    valid = 0
    for line in lines:
        split = line.split(' ')
        occurrences = split[0].split('-')

        # -1 because they are 0-indexed
        position1 = int(occurrences[0]) - 1
        position2 = int(occurrences[1]) - 1
        letter = (split[1])[0]
        password = split[-1]

        count = 1 if password[position1] == letter else 0
        count = count + (1 if password[position2] == letter else 0)
        if count == 1:
            valid = valid + 1

    return valid


if __name__ == '__main__':
    with open('day2input.txt', 'r') as file:
        file_lines = file.readlines()
        print('Part 1', count_valid_passwords_part1(file_lines))
        print('Part 2', count_valid_passwords_part2(file_lines))
