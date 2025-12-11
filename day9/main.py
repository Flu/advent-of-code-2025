from functools import lru_cache

TEST = False

def area_between_points(p1, p2):
    return abs(p1[0] - p2[0] + 1) * abs(p1[1] - p2[1] + 1)

red_tiles = []
with open("test.in" if TEST else "data.in", "r") as f:
    while line := f.readline():
        coords = line.split(",")
        red_tiles.append((int(coords[0]), int(coords[1])))

# PART 1
biggest_area = 0

for i, corner1 in enumerate(red_tiles):
    for j, corner2 in enumerate(red_tiles):
        if j > i:
            area = area_between_points(corner1, corner2)
            if area > biggest_area:
                biggest_area = area

print("Part 1:", biggest_area)

# PART 2
# What the fuck, I can't solve this
print("Part 2:")
