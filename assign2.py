import heapq

# Function to print the puzzle
def print_puzzle(puzzle):
    for i in range(3):
        print(puzzle[i*3 : (i+1)*3]) # Slice the list to get rows
    print()

# Function to calculate Manhattan Distance heuristic
def heuristic(state, goal):
    h = 0
    for i in range(9):
        if state[i] == -1:  # Ignore the empty tile
            continue
        goal_index = goal.index(state[i])
        h += abs(i // 3 - goal_index // 3) + abs(i % 3 - goal_index % 3)
    return h

# Function to get possible moves
def get_moves(state):
    empty_index = state.index(-1)
    moves = []
    row, col = empty_index // 3, empty_index % 3

    if col > 0:  # Move Left
        moves.append((empty_index - 1, "Left"))
    if col < 2:  # Move Right
        moves.append((empty_index + 1, "Right"))
    if row > 0:  # Move Up
        moves.append((empty_index - 3, "Up"))
    if row < 2:  # Move Down
        moves.append((empty_index + 3, "Down"))

    return moves

# A* algorithm to solve 8-puzzle
def solve_puzzle(start, goal):
    priority_queue = []
    heapq.heappush(priority_queue, (heuristic(start, goal), 0, start, []))  # (f, g, state, path)
    visited = set()

    while priority_queue:
        _, g, current_state, path = heapq.heappop(priority_queue)

        if current_state == goal:
            print("Solved in", g, "moves!")
            for move in path:
                print(move)
            return

        visited.add(tuple(current_state))

        for move, direction in get_moves(current_state):
            new_state = current_state[:]
            new_state[current_state.index(-1)], new_state[move] = new_state[move], new_state[current_state.index(-1)]

            if tuple(new_state) not in visited:
                heapq.heappush(priority_queue, (g + 1 + heuristic(new_state, goal), g + 1, new_state, path + [direction]))

    print("Impossible to solve!")

# Check if the puzzle is solvable based on inversions
def is_solvable(state):
    nums = [num for num in state if num != -1]  # Remove the empty space (-1)
    
    inversions = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):  # Compare every number with those after it
            if nums[i] > nums[j]:  # Inversion if the first number is larger than the second
                inversions += 1
    
    return inversions % 2 == 0  # If inversions is even, puzzle is solvable

# Input and execution
start = list(map(int, input("Enter start state (-1 for empty, space-separated): ").split()))
goal = list(map(int, input("Enter goal state (-1 for empty, space-separated): ").split()))

print("\nStart State:")
print_puzzle(start)

if is_solvable(start):
    solve_puzzle(start, goal)
else:
    print("Impossible to Solve!")


# Output:
'''
Enter start state (-1 for empty, space-separated): 1 2 3 -1 4 6 7 5 8
Enter goal state (-1 for empty, space-separated): 1 2 3 4 5 6 7 8 -1

Start State:
[1, 2, 3]
[-1, 4, 6]
[7, 5, 8]

Solved in 3 moves!
Right
Down
Right
'''