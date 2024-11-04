"""
* Entrada:
*   - N: int
*   - position: array
*   - opponents: array
*   - K: int
*
* Saída: int
"""
def knightAttack(N, position, opponents, K):
    from collections import deque

    # Movimentos possíveis do cavalo
    moves = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]
    
    # Inicializa a fila com a posição inicial do cavalo
    queue = deque([(position[0], position[1], 0, set())])
    
    # Inicializa o conjunto de oponentes capturados
    max_captures = 0
    
    # Converte a lista de oponentes para um conjunto de tuplas
    opponents_set = {tuple(opponent) for opponent in opponents}
    
    while queue:
        x, y, steps, captured = queue.popleft()
        
        if steps > K:
            continue
        
        max_captures = max(max_captures, len(captured))
        
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < N and 0 <= ny < N:
                new_captured = set(captured)
                if (nx, ny) in opponents_set and (nx, ny) not in new_captured:
                    new_captured.add((nx, ny))
                queue.append((nx, ny, steps + 1, new_captured))
    
    return max_captures

# Teste da função
N = 8
position = [3, 2]
opponents = [[5, 1], [4, 5], [5, 4]]
K = 1

print(knightAttack(N, position, opponents, K))  # Output esperado: 1