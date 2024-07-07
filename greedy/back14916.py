#거스름돈
def min_coins(n):
    five_coins = n // 5
    for i in range(five_coins, -1, -1):
        two_coins = n - (i * 5)
        if two_coins % 2 == 0:
            return i + (two_coins // 2)
    return -1
  
n = int(input())
print(min_coins(n))
