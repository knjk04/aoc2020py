def sum_of_yeses(answers: [str]) -> int:
    # special case: newline represents end of group, so we add an extra one to the end if it's not
    # already there
    if answers[-1] != '\n':
        answers.append('\n')

    count = 0
    unique_answers = {}
    for answer in answers:
        if answer == '\n':
            count = count + len(unique_answers)
            unique_answers = {}  # reset
        else:
            if answer[-1] == '\n':
                answer = answer.removesuffix('\n')
            [unique_answers.setdefault(char, 1) for char in answer]  # value set is irrelevant

    return count


# TODO: fix. Answer is too low
def sum_of_yeses_part2(answers: [str]) -> int:
    # special case: newline represents end of group, so we add an extra one to the end if it's not
    # already there
    if answers[-1] != '\n':
        answers.append('\n')

    count = 0
    num_people = 0
    answers_dict = {}
    for answer in answers:
        reached_end_of_group = answer == '\n'
        if reached_end_of_group:
            if num_people == 1:
                count = count + len(answers_dict)
            elif len(answers_dict) == 1:
                count = count + 1
            else:
                answered_yes_to_all = True
                for v in answers_dict.values():
                    if v != num_people:
                        answered_yes_to_all = False
                        break
                    else:
                        count = count + 1
                if answered_yes_to_all:
                    count = count + len(answers_dict)

            answers_dict = {}  # reset
            num_people = 0  # reset
        else:
            if answer[-1] == '\n':
                answer = answer.removesuffix('\n')
            for char in answer:
                if char in answers_dict:
                    answers_dict[char] = answers_dict[char] + 1
                else:
                    answers_dict[char] = 1
            num_people = num_people + 1

    return count


if __name__ == '__main__':
    with open('day6input.txt', 'r') as file:
        batch = file.readlines()
        # print('Part 1:', sum_of_yeses(batch))
        print('Part 2:', sum_of_yeses_part2(batch))
