from collections import Counter

def remove_one_beam(beam, beams):
    for i in range(len(beams)):
        if beams[i] == beam:
            del beams[i]
            return
    
def follow_beam(matrix: list[list[int]], start_x: int, start_y: int, limit_x: int) -> int:
    beams = [start_y]
    x = start_x

    beam_splits = 0
    
    while x < limit_x:
        for idx, beam in enumerate(beams[:]):
            if matrix[x][beam] == '^':
                beam_splits += 1
                if (beam - 1) not in beams:
                    beams.append(beam-1)
                if (beam + 1) not in beams:
                    beams.append(beam+1)
                # Remove only one instance of beam
                remove_one_beam(beam, beams)
        x += 1
    return beam_splits

def count_timelines_rec(matrix: list[list[int]], start_x: int, start_y: int, limit_x: int):
    x = start_x

    while True:
        x += 1
        if x >= limit_x:
            return 1
        if matrix[x][start_y] == '^':
            return follow_beam_rec(matrix, x, start_y - 1, limit_x) + follow_beam_rec(matrix, x, start_y + 1, limit_x)

def count_timelines(grid: list[list[int]], start_r: int, start_c: int):
    beams = Counter({start_c: 1})

    for row in grid[start_r + 1:]:
        next_beams = Counter()
        for col, count in beams.items():
            if row[col] == '^':
                next_beams[col - 1] += count
                next_beams[col + 1] += count
            else:
                next_beams[col] += count
        beams = next_beams

    return sum(beams.values())

matrix = []
starting_pos = (0,0)
with open("data.in", "r") as f:
    while line := f.readline().strip():
        matrix.append([])
        for char in line:
            if char == 'S':
                starting_pos = (len(matrix)-1, len(matrix[-1]))
            matrix[-1].append(char)

print(follow_beam(matrix, starting_pos[0], starting_pos[1], len(matrix)))
print(count_timelines(matrix, starting_pos[0], starting_pos[1]))
