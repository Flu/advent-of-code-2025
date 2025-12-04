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

def update_neighbours(paper_rolls, neighbour_matrix, work_queue, i, j):
    def is_valid_index(row, col):
        rows = len(paper_rolls)
        cols = len(paper_rolls[0])
        if row < 0 or row > rows - 1:
            return False
        if col < 0 or col > cols - 1:
            return False
        return True

    if is_valid_index(i-1, j-1) and paper_rolls[i-1][j-1] == '@':
        neighbour_matrix[i-1][j-1] -= 1
        if neighbour_matrix[i-1][j-1] < 4 and (i-1,j-1) not in work_queue:
            work_queue.append((i-1,j-1))

    if is_valid_index(i-1, j) and paper_rolls[i-1][j] == '@':
        neighbour_matrix[i-1][j] -= 1
        if neighbour_matrix[i-1][j] < 4 and (i-1,j) not in work_queue:
            work_queue.append((i-1,j))

    if is_valid_index(i-1, j+1) and paper_rolls[i-1][j+1] == '@':
        neighbour_matrix[i-1][j+1] -= 1
        if neighbour_matrix[i-1][j+1] < 4 and (i-1,j+1) not in work_queue:
            work_queue.append((i-1,j+1))

    if is_valid_index(i, j-1) and paper_rolls[i][j-1] == '@':
        neighbour_matrix[i][j-1] -= 1
        if neighbour_matrix[i][j-1] < 4 and (i,j-1) not in work_queue:
            work_queue.append((i,j-1))

    if is_valid_index(i, j+1) and paper_rolls[i][j+1] == '@':
        neighbour_matrix[i][j+1] -= 1
        if neighbour_matrix[i][j+1] < 4 and (i,j+1) not in work_queue:
            work_queue.append((i,j+1))

    if is_valid_index(i+1, j-1) and paper_rolls[i+1][j-1] == '@':
        neighbour_matrix[i+1][j-1] -= 1
        if neighbour_matrix[i+1][j-1] < 4 and (i+1,j-1) not in work_queue:
            work_queue.append((i+1,j-1))

    if is_valid_index(i+1, j) and paper_rolls[i+1][j] == '@':
        neighbour_matrix[i+1][j] -= 1
        if neighbour_matrix[i+1][j] < 4 and (i+1,j) not in work_queue:
            work_queue.append((i+1,j))

    if is_valid_index(i+1, j+1) and paper_rolls[i+1][j+1] == '@':
        neighbour_matrix[i+1][j+1] -= 1
        if neighbour_matrix[i+1][j+1] < 4 and (i+1,j+1) not in work_queue:
            work_queue.append((i+1,j+1))
        
def find_and_remove_rolls(paper_rolls) -> int:
    work_queue = []
    neighbour_matrix = [([0]*len(paper_rolls[0])) for i in range(len(paper_rolls))]

    # Initial Pass
    for i in range(len(paper_rolls)):
        for j in range(len(paper_rolls[0])):
            if paper_rolls[i][j] == '@':
                neighbours = num_neighbours(paper_rolls, i, j)
                neighbour_matrix[i][j] = neighbours
                if neighbours < 4:
                    work_queue.append((i,j))

    # Start the queue
    removed_rolls = 0
    while len(work_queue) != 0:
        roll = work_queue.pop(0)
        paper_rolls[roll[0]][roll[1]] = 'x'
        update_neighbours(paper_rolls, neighbour_matrix, work_queue, roll[0], roll[1])
        removed_rolls += 1

    return removed_rolls
    
    
with open("data.in", "r") as f:
    paper_rolls = []
    
    while line := f.readline().strip():
        paper_rolls.append([])
        for roll in line:
            paper_rolls[-1].append(roll)

    total = find_and_remove_rolls(paper_rolls)
    print(total)
