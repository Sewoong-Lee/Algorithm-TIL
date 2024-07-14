#사탕
T = int(input().strip())
results = []
for _ in range(T):
    J, N = map(int, input().split())
    boxes = []
    for _ in range(N):
        R, C = map(int, input().split())
        boxes.append(R * C)
    boxes.sort(reverse=True)
    candies = J
    boxCount = 0
    for box in boxes:
        if candies <= 0:
            break
        candies -= box
        boxCount += 1
    results.append(boxCount)
for result in results:
    print(result)
