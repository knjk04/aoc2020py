def count_valid_passwords(lines: [str]) -> int:
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


if __name__ == '__main__':
    with open('day2input.txt', 'r') as file:
        num_valid = count_valid_passwords(file.readlines())
        print(num_valid)
