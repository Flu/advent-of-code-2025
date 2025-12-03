def largest_joltage(joltages: [int], radix: int = 2) -> int:
    max_num = [-1]*(radix)

    for r in range(radix):
        if r == 0:
            max_num[0] = 0
        else:
            max_num[r] = max_num[r-1] + 1
            
        for index in range(max_num[r], len(joltages) - (radix - (r + 1))):
            if joltages[index] > joltages[max_num[r]]:
                max_num[r] = index

    final_joltage = 0
    max_num = max_num[::-1]
    for r in range(radix):
        final_joltage += joltages[max_num[r]] * 10**r
    return final_joltage

with open("data.in", "r") as f:
    total_joltage_part1 = 0
    total_joltage_part2 = 0
    while line := f.readline():
        battery_bank = []
        for char in line:
            if char != '\n':
                battery_bank.append(int(char))
                
        total_joltage_part1 += largest_joltage(battery_bank, radix=2)
        total_joltage_part2 += largest_joltage(battery_bank, radix=12)

    print(total_joltage_part1)
    print(total_joltage_part2)
