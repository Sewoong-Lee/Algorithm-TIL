#헌내기는 친구가 필요해
N, M = map(int, input().split())
cam = [list(input()) for _ in range(N)]

d = [(-1, 0), (1, 0), (0, -1), (0, 1)]

start_x, start_y = 0, 0
for i in range(N):
    for j in range(M):
        if cam[i][j] == 'I':
            start_x, start_y = i, j
            break
          
q = [(start_x, start_y)]
v = [[False] * M for _ in range(N)]
v[start_x][start_y] = True
count = 0

while q:
    x, y = q.pop(0)
    for dx, dy in d:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M and not v[nx][ny]:
            if cam[nx][ny] != 'X':  # 벽이 아닌 경우
                v[nx][ny] = True
                q.append((nx, ny))
                if cam[nx][ny] == 'P':
                    count += 1
if count > 0:
    print(count)
else:
    print("TT")
