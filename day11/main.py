from functools import lru_cache

TEST = False

graph = dict()
with open("test.in" if TEST else "data.in", "r") as f:
    while line := f.readline():
        parts = line.strip().split(":")
        source = parts[0].strip()
        devices = parts[1].strip().split(" ")

        graph[source] = devices

# PART 1
def count_paths(source_node):
    if source_node == "out":
        return 1
    
    sum_of_grandchildren = 0
    for child in graph[source_node]:
        sum_of_grandchildren += count_paths(child)

    return sum_of_grandchildren

print("Part 1:", count_paths("you"))

# PART 2
graph = dict()
with open("test2.in" if TEST else "data.in", "r") as f:
    while line := f.readline():
        parts = line.strip().split(":")
        source = parts[0].strip()
        devices = parts[1].strip().split(" ")

        graph[source] = devices

@lru_cache(maxsize=1000)
def count_paths_through_dac_fft(source_node, dac=False, fft=False):
    if source_node == "out" and dac and fft:
        return 1
    elif source_node == "out":
        return 0
    
    sum_of_grandchildren = 0
    for child in graph[source_node]:
        new_dac = dac or source_node == "dac"
        new_fft = fft or source_node == "fft"
        paths = count_paths_through_dac_fft(child, new_dac, new_fft)

        sum_of_grandchildren += paths

    return sum_of_grandchildren

print("Part 2:", count_paths_through_dac_fft("svr"))
