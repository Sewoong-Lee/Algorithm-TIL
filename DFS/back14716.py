#현수막
M, N = map(int, input().split())
banner = []

for _ in range(M):
  banner.append(list(map(int, input().split())))

direction = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
  
# def dfsFun(x,y):
#   banner[x][y] = 0
#   for dx, dy in direction:
#     if 0 <= x+dx < M and 0 <= y+dy < N and banner[x+dx][y+dy] == 1:
#       dfsFun(x+dx, y+dy)

def dfsFun(x, y):
    stack = [(x, y)]
    while stack:
        sx, sy = stack.pop()
        if banner[sx][sy] == 1:
            banner[sx][sy] = 0 
            for dx, dy in direction:
                if 0 <= sx + dx < M and 0 <= sy + dy < N and banner[sx + dx][sy + dy] == 1:
                    stack.append((sx + dx, sy + dy))
      
ctn = 0

for m in range(M):
  for n in range(N):
    if banner[m][n] == 1:
      dfsFun(m,n)
      ctn += 1
      
print(ctn)