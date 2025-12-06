from functools import reduce
import operator

# PART 1

def solve_equations(equations) -> list[int]:
    answers = []
    for eq in equations:
        if eq[-1] == '+':
            answers.append(sum(eq[0:-1]))
        elif eq[-1] == '*':
            answers.append(reduce(lambda x, y: x*y, eq[0:-1]))
    return answers

with open("data.in", "r") as f:
    lines = f.readlines()
    
    math_problems = []
    for i in range(len(lines[0].split())):
        math_problems.append([])

    for i in range(len(lines)):
        numbers = lines[i].split()
        for idx, number in enumerate(numbers):
            if number != '*' and number != '+':
                number = int(number)
            math_problems[idx].append(number)
    print("Part 1: ", sum(solve_equations(math_problems)))

# PART 2

with open("data.in", "r") as f:
    lines = [line.rstrip("\n") for line in f]

max_width = max(len(line) for line in lines)
columns = [[] for _ in range(max_width)]

for line in lines:
    for col, ch in enumerate(line.ljust(max_width)):
        if ch.isdigit():
            columns[col].append(ch)
        elif ch in '+*':
            columns[col].append(ch)
        else:
            columns[col].append(' ')

answers = []
current_nums = []
current_op = None

def all_spaces(col):
    return all(ch == ' ' for ch in col)

def extract_digits(col):
    return ''.join(ch for ch in col if ch.isdigit())

for col in columns:
    if all_spaces(col):
        if current_nums:
            if current_op == '*':
                block_value = reduce(operator.mul, current_nums, 1)
            else:
                block_value = sum(current_nums)
            answers.append(block_value)
            current_nums = []
            current_op = None
        continue

    for ch in col:
        if ch in '+*':
            current_op = ch

    num_str = extract_digits(col)
    if num_str:
        current_nums.append(int(num_str))

if current_nums:
    if current_op == '*':
        block_value = reduce(operator.mul, current_nums, 1)
    else:
        block_value = sum(current_nums)
    answers.append(block_value)

print("Part 2: ", sum(answers))
