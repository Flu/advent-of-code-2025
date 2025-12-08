from functools import reduce

TEST = False

def distance(j1, j2):
    return (j1[0]-j2[0])**2 + (j1[1]-j2[1])**2 + (j1[2]-j2[2])**2

def which_circuit(junction, circuits):
    for i, c in enumerate(circuits):
        if junction in c:
            return i
    return -1

def start_connecting(sorted_pairs, limit=1000, return_last_pair=False):
    circuits = []
    last_pair_to_connect = None
    
    for shortest in range(limit):
        p = pairs[shortest]

        # Find in which circuit is j1 and j2
        j1 = which_circuit(p[0], circuits)
        j2 = which_circuit(p[1], circuits)
        # If neither are in a circuit, create a new circuit and add them both to it
        if j1 == -1 and j2 == -1:
            circuits.append([p[0], p[1]])
            last_pair_to_connect = p[0], p[1]
            # If j1 is in a circuit and j2 is not, add j2 to j1's circuit
        elif j1 != -1 and j2 == -1:
            circuits[j1].append(p[1])
            last_pair_to_connect = p[0], p[1]
            # If j2 is in a circuit and j2 is not, add j1 to j2's circuit
        elif j1 == -1 and j2 != -1:
            circuits[j2].append(p[0])
            last_pair_to_connect = p[0], p[1]
            # If both are in different circuits, merge circuits
        elif j1 != j2:
            circuits[j1] += circuits[j2]
            del circuits[j2]
            last_pair_to_connect = p[0], p[1]

        if len(circuits) == 1 and len(circuits[0]) == len(sorted_pairs)*2:
            break

    if return_last_pair:
        return last_pair_to_connect
    return circuits

junctions = []
pairs = []

with open("test.in" if TEST else "data.in", "r") as f:
    while line := f.readline():
        coords = line.split(",")
        junctions.append((int(coords[0]), int(coords[1]), int(coords[2])))
        
for i, j1 in enumerate(junctions):
    for j, j2 in enumerate(junctions):
        if i != j and j > i:
            pairs.append((i, j, distance(j1, j2)))

# PART 1
pairs.sort(key=lambda x: x[2])
circuits = start_connecting(pairs, limit=10 if TEST else 1000)
print("Part 1:", reduce(lambda x, y: x*y, list(map(lambda x: len(x), sorted(circuits, key=lambda l: len(l), reverse=True)))[:3], 1))

# PART 2
last_pair_to_connect = start_connecting(pairs, limit=len(pairs), return_last_pair=True)
print("Part 2:", junctions[last_pair_to_connect[0]][0]*junctions[last_pair_to_connect[1]][0])
