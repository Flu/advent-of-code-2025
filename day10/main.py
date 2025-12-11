from z3 import *

TEST = False

def push_buttons(state: tuple[int, ...], choice: list[int]) -> tuple[int, ...]:
    s = list(state)
    for c in choice:
        s[c] ^= 1
    return tuple(s)

def adjust_joltage(state: tuple[int, ...], choice: list[int]) -> tuple[int, ...]:
    s = list(state)
    for c in choice:
        s[c] += 1
    return tuple(s)

class Machine:
    def __init__(self, button_states: str, choices: list[list[int]]):
        buttons = [0]*len(button_states)
        self.choices = choices[:]
        
        for idx, b in enumerate(button_states):
            if b == '.':
                buttons[idx] = 0
            else:
                buttons[idx] = 1
        self.buttons = tuple(buttons)

    def find_shortest_sequence(self):
        queue: list[tuple[tuple[int, ...], int]] = [(self.buttons, 0)]
        visited = set()
        end_state = (0,)*len(self.buttons)
        
        while len(queue) != 0:
            current_state = queue.pop(0)
            for c in self.choices:
                new_state = push_buttons(current_state[0], c)
                if new_state == end_state:
                    return current_state[1] + 1
                if new_state not in visited:
                    visited.add(new_state)
                    queue.append((new_state, current_state[1]+1))
        return 0

    def find_joltage_shortest_sequence(self, end_state):
        num_buttons = len(self.choices)
        num_counters = len(end_state)
        
        opt = Optimize()
        
        x = [Int(f"x_{j}") for j in range(num_buttons)]
        
        for j in range(num_buttons):
            opt.add(x[j] >= 0)
            
        for i in range(num_counters):
            opt.add(sum(
                (1 if i in self.choices[j] else 0) * x[j]
                for j in range(num_buttons)
            ) == end_state[i])
                
        opt.minimize(sum(x))
                
        if opt.check() != sat:
            raise RuntimeError("No solution")
                
        model = opt.model()
                
        presses = [model[x[j]].as_long() for j in range(num_buttons)]
        return sum(presses)
        
sum_of_presses_part1 = 0
sum_of_presses_part2 = 0

with open("test.in" if TEST else "data.in", "r") as f:
    while line := f.readline():
        parts = line.split(' ')

        button_states = parts[0][1:-1]
        joltage_requirements = None
        choices = []
        
        for choice in parts[1:-1]:
            choice_without_parens = choice[1:-1]
            indices = list(map(int, choice_without_parens.split(',')))
            choices.append(indices)

        joltage_requirements = [int(x) for x in parts[-1].strip()[1:-1].split(",")]
        
        machine = Machine(button_states, choices)
        sum_of_presses_part1 += machine.find_shortest_sequence()
        sum_of_presses_part2 += machine.find_joltage_shortest_sequence(joltage_requirements)
        
print("Part 1:", sum_of_presses_part1)
print("Part 2:", sum_of_presses_part2)
