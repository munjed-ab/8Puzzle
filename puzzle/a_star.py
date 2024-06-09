
import heapq

def heuristic(state, goal):
    def manhattan_distance(idx1, idx2):
        x1, y1 = divmod(idx1, 3)
        x2, y2 = divmod(idx2, 3)
        return abs(x1 - x2) + abs(y1 - y2)

    distance = 0
    for num in range(1, 9):
        distance += manhattan_distance(state.index(str(num)), goal.index(str(num)))
    return distance

def get_neighbors(state):
    neighbors = []
    try:
        zero_idx = state.index(' ')
    except ValueError:
        return neighbors  # Return empty list if blank space not found
    x, y = divmod(zero_idx, 3)
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_idx = nx * 3 + ny
            new_state = list(state)
            new_state[zero_idx], new_state[new_idx] = new_state[new_idx], new_state[zero_idx]
            neighbors.append(''.join(new_state))
    return neighbors

def a_star(start, goal):
    open_set = []
    heapq.heappush(open_set, (0, start))
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, goal)}

    while open_set:
        current = heapq.heappop(open_set)[1]

        if current == goal:
            return reconstruct_path(came_from, current)

        for neighbor in get_neighbors(current):
            tentative_g_score = g_score[current] + 1  # cost between neighbors is 1

            if tentative_g_score < g_score.get(neighbor, float('inf')):
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                heapq.heappush(open_set, (f_score[neighbor], neighbor))

    return None  # No solution found

def reconstruct_path(came_from, current):
    total_path = [current]
    while current in came_from:
        current = came_from[current]
        total_path.append(current)
    return total_path[::-1]
