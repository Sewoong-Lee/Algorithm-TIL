# 한 줄로 서기
N = int(input())
leftNum = list(map(int, input().split()))
lineList = [0] * N

for i in range(N):
    c = leftNum[i]
    position = 0
    for j in range(N):
        if lineList[j] == 0: 
            if c == 0:
                lineList[j] = i + 1
                break
            c -= 1
print(' '.join(map(str, lineList)))
