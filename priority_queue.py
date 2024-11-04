"""
* Entrada:
* - grid (list)
* - amount (int)
*
* Saída: string
"""
def findMinCost(grid, amount):
    import heapq
    
    rows, cols = len(grid), len(grid[0])
    directions = [(0, 1), (1, 0), (1, 1)]  # Direita, Baixo, Diagonal
    heap = [(grid[0][0], 0, 0)]  # (custo atual, posição x, posição y)
    visited = set()

    while heap:
        current_cost, x, y = heapq.heappop(heap)

        if (x, y) in visited:
            continue

        visited.add((x, y))

        if x == rows - 1 and y == cols - 1:
            return current_cost if current_cost <= amount else -1

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited:
                new_cost = current_cost + grid[nx][ny]
                heapq.heappush(heap, (new_cost, nx, ny))

    return -1

# Teste da função
grid1 = [
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 0]
]
amount1 = 10

grid2 = [
    [1, 2, 1],
    [4, 5, 2],
    [1, 1, 1],
    [3, 5, 0]
]
amount2 = 4

print(findMinCost(grid1, amount1))  # Output esperado: 4
print(findMinCost(grid2, amount2))  # Output esperado: -1