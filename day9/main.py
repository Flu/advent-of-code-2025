
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
                print(corner1, corner2)

print("Part 1:", biggest_area)

# PART 2

def on_boundary(point, red_tiles):
    x, y = point
    n = len(red_tiles)
    for i in range(n):
        x1, y1 = red_tiles[i]
        x2, y2 = red_tiles[(i + 1) % n]
        if (x, y) == (x1, y1) or (x, y) == (x2, y2):
            continue

        if y1 == y2 == y:
            if min(x1, x2) < x < max(x1, x2):
                return True

        if x1 == x2 == x:
            if min(y1, y2) < y < max(y1, y2):
                return True

    return False


def inside_polygon(point, red_tiles):
    x, y = point
    intersections = 0
    n = len(red_tiles)

    for i in range(n):
        x1, y1 = red_tiles[i]
        x2, y2 = red_tiles[(i + 1) % n]

        if x1 != x2:
            continue

        if min(y1, y2) < y <= max(y1, y2):
            if x < x1:
                intersections += 1

    return (intersections % 2) == 1

def is_green_tile(point, red_tiles):
    return on_boundary(point, red_tiles) or inside_polygon(point, red_tiles)

def find_largest_valid_rectangle(red_tiles):
    red_set = set(red_tiles)
    biggest_area_rect = 0
    best_corners = None

    n = len(red_tiles)
    for i in range(n):
        x1, y1 = red_tiles[i]
        for j in range(i+1, n):
            x2, y2 = red_tiles[j]

            # must be opposite corners of an axis-aligned rectangle
            if x1 == x2 or y1 == y2:
                continue

            # compute bounding coordinates
            min_x, max_x = min(x1, x2), max(x1, x2)
            min_y, max_y = min(y1, y2), max(y1, y2)

            # quick area test
            area = area_between_points((x1, y1), (x2, y2))
            if area <= biggest_area_rect:
                # can't beat current best
                continue

            valid = True
            # check every tile inside rectangle (including border/corners)
            for xx in range(min_x, max_x + 1):
                if not valid:
                    break
                for yy in range(min_y, max_y + 1):
                    pt = (xx, yy)
                    # corners are guaranteed red (since we chose them),
                    # allow any red tile
                    if pt in red_set:
                        continue
                    # otherwise it must be green (either boundary or inside)
                    if not is_green_tile(pt, red_tiles):
                        valid = False
                        break

            if valid:
                biggest_area_rect = area
                best_corners = ((x1, y1), (x2, y2))

    return biggest_area_rect, best_corners


area2, corners2 = find_largest_valid_rectangle(red_tiles)
print("Part 2:", area2, corners2)
