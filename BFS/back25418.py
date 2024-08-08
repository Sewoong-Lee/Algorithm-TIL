#정수 a를 k로 만들기
A, K = map(int, input().split())
queue = [(A, 0)]  
alreadyCals = set([A])

while queue:
    currentNum, operationNum = queue.pop(0)
    if currentNum == K:
        print(operationNum)
        break
    if currentNum + 1 <= K and currentNum + 1 not in alreadyCals:
        alreadyCals.add(currentNum + 1)
        queue.append((currentNum + 1, operationNum + 1))
    if currentNum * 2 <= K and currentNum * 2 not in alreadyCals:
        alreadyCals.add(currentNum * 2)
        queue.append((currentNum * 2, operationNum + 1))
