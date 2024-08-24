#[투포인터]고양이 카페
N, K = map(int, input().split())
wList = list(map(int, input().split()))
wList.sort()

lef = 0
rig = N - 1
count = 0

while lef < rig:
    if wList[lef] + wList[rig] <= K:
        count += 1
        lef += 1  
        rig -= 1  
    else:
        rig -= 1

print(count)
