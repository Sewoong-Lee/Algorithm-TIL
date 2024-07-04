#5와 6의 차이
A, B = input().split()

minA = int(A.replace('6', '5'))
minB = int(B.replace('6', '5'))
minSum = minA + minB

maxA = int(A.replace('5', '6'))
maxB = int(B.replace('5', '6'))
maxSum = maxA + maxB

print(minSum, maxSum)