# Alternative approach: use file.read().splitlines(), then sort the list. Next, iterate over each
# element in the list and do a binary search to see whether the number needed to sum to 2020 is in
# the list
def calc_product_part1(lines: [str]) -> int:
    for index, line in enumerate(lines):
        entry = int(line.strip())
        if entry > 2020:
            continue
        for line2 in lines[index+1:]:
            if entry + int(line2) == 2020:
                return entry * int(line2)


def calc_product_part2(lines: [str]) -> int:
    for index, line in enumerate(lines):
        operand1 = int(line.strip())
        if operand1 > 2020:
            continue
        for line2 in lines[index+1:]:
            operand2 = int(line2)
            if operand2 > 2020 or operand1 + operand2 > 2020:
                continue
            for line3 in lines[index+2:]:
                operand3 = int(line3)
                if operand1 + operand2 + operand3 == 2020:
                    return operand1 * operand2 * operand3


if __name__ == '__main__':
    with open('day1input.txt', 'r') as file:
        expense_report = file.readlines()
        print('Part 1:', calc_product_part1(expense_report))
        print('Part 2:', calc_product_part2(expense_report))
