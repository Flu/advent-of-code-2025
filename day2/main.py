def is_invalid_id(id_str: str) -> bool:
    n = len(id_str)
    if n % 2 != 0:
        return False

    half = n // 2
    first = id_str[:half]
    second = id_str[half:]

    return first == second

def is_invalid_id_2(s: str) -> bool:
    n = len(s)
    for k in range(1, n//2 + 1):
        if n % k == 0:
            part = s[:k]
            if part * (n // k) == s:
                return True
    return False

# Part 1
s = 0
with open("data.in", "r") as f:
    line = f.readline()
    for id_range in line.split(","):
        [start, end] = id_range.split("-")
        for id_int in range(int(start), int(end)+1):
            if is_invalid_id(str(id_int)):
                s += id_int

print(s)

# Part 2
s = 0
with open("data.in", "r") as f:
    line = f.readline()
    for id_range in line.split(","):
        [start, end] = id_range.split("-")
        for id_int in range(int(start), int(end)+1):
            if is_invalid_id_2(str(id_int)):
                s += id_int

print(s)
