def calc_product(lines: [str]) -> int:
    for index, line in enumerate(lines):
        entry = int(line.strip())
        if entry > 2020:
            continue
        for line2 in lines[index+1:]:
            if entry + int(line2) == 2020:
                return entry * int(line2)


if __name__ == '__main__':
    with open('day1input.txt', 'r') as file:
        product = calc_product(file.readlines())
        print(product)
