#빠른 숫자 탐색
board = []
for _ in range(5):
    board.append(list(map(int, input().split())))
r, c = map(int, input().split())

q = [(r, c, 0)]
already = []
for _ in range(5):
    row = [False] * 5
    already.append(row)

already[r][c] = True
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

while q:
    cr, cc, moves = q.pop(0)
    if board[cr][cc] == 1:
        print(moves)
        break
      
    for dr, dc in direction:
        nr, nc = cr + dr, cc + dc
        if 0 <= nr < 5 and 0 <= nc < 5 and not already[nr][nc] and board[nr][nc] != -1:
            already[nr][nc] = True
            q.append((nr, nc, moves + 1))
else:
    print(-1)
