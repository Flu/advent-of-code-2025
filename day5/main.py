ranges = []

with open("data.in", "r") as f:
    while line := f.readline().strip():
        if line == '':
            break
        line = line.split("-")
        ranges.append((int(line[0]),int(line[1])))

    ingredients = []
    while line := f.readline():
        ingredients.append(int(line))

    fresh_ingredients = []
    for ingredient in ingredients:
        for r in ranges:
            if ingredient in range(r[0], r[1]+1) and ingredient not in fresh_ingredients:
                fresh_ingredients.append(ingredient)

    print("Part 1: ", len(fresh_ingredients))

    ranges.sort()

    merged_ranges = []
    curr_start, curr_end = ranges[0]
    for start, end in ranges[1:]:
        if start <= curr_end + 1:
            curr_end = max(curr_end, end)
        else:
            merged_ranges.append((curr_start, curr_end))
            curr_start, curr_end = start, end

    merged_ranges.append((curr_start, curr_end))

    # count lengths
    total_fresh_ingredients = sum(e - s + 1 for s, e in merged_ranges)
    
    print("Part 2: ", total_fresh_ingredients)
