# 점프 점프
def dfs(pos, stoneList, checkList):
    checkList[pos] = True
    curJump = stoneList[pos] 
    
    left = pos - curJump
    if left >= 0:
        if not checkList[left]:
            dfs(left, stoneList, checkList)
    right = pos + curJump
    if right < len(stoneList):
        if not checkList[right]:
            dfs(right, stoneList, checkList)

n = int(input())
stoneList = list(map(int, input().split()))
s = int(input()) - 1  

checkList = [False for _ in range(n)] 

dfs(s, stoneList, checkList)

print(checkList.count(True))
