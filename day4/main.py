def num_neighbours(paper_rolls, row, col) -> int:
    def is_valid_index(row, col):
        rows = len(paper_rolls)
        cols = len(paper_rolls[0])
        if row < 0 or row > rows - 1:
            return False
        if col < 0 or col > cols - 1:
            return False
        return True

    neighbours = 0
    if is_valid_index(row-1, col-1) and paper_rolls[row-1][col-1] == '@':
        neighbours += 1
        
    if is_valid_index(row-1, col) and paper_rolls[row-1][col] == '@':
        neighbours += 1
        
    if is_valid_index(row-1, col+1) and paper_rolls[row-1][col+1] == '@':
        neighbours += 1
        
    if is_valid_index(row, col-1) and paper_rolls[row][col-1] == '@':
        neighbours += 1
        
    if is_valid_index(row, col+1) and paper_rolls[row][col+1] == '@':
        neighbours += 1
        
    if is_valid_index(row+1, col-1) and paper_rolls[row+1][col-1] == '@':
        neighbours += 1
        
    if is_valid_index(row+1, col) and paper_rolls[row+1][col] == '@':
        neighbours += 1
        
    if is_valid_index(row+1, col+1) and paper_rolls[row+1][col+1] == '@':
        neighbours += 1
        
    return neighbours

def find_and_remove_rolls(paper_rolls) -> int:
    rolls_that_can_be_removed = []
    for i in range(len(paper_rolls)):
        for j in range(len(paper_rolls[0])):
            if paper_rolls[i][j] == '@' and num_neighbours(paper_rolls, i, j) < 4:
                rolls_that_can_be_removed.append((i,j))

    ret = len(rolls_that_can_be_removed)
    for roll in rolls_that_can_be_removed:
        paper_rolls[roll[0]][roll[1]] = '.'
    return ret
    
    
with open("data.in", "r") as f:
    paper_rolls = []
    
    while line := f.readline().strip():
        paper_rolls.append([])
        for roll in line:
            paper_rolls[-1].append(roll)

    total = 0
    while rolls_removed := find_and_remove_rolls(paper_rolls):
        total += rolls_removed
    print(total)
