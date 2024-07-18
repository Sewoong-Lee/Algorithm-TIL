#바닥 장식
N, M = map(int, input().split())
all = []

for n in range(N):
  all.append(list(input()))
  
def dfsFun(x,y,shape):
  all[x][y] = True
  if shape == '|':
    if x+1 < N and all[x+1][y] == shape:
        dfsFun(x +1 ,y,shape)
  elif shape == '-':
    if y+1 < M and all[x][y+1] == shape:
        dfsFun(x,y+1,shape)

ctn = 0

for n in range(N):
  for m in range(M):
    if all[n][m] == '-' or all[n][m] == '|':
      dfsFun(n,m, all[n][m])
      ctn += 1
      
print(ctn)

