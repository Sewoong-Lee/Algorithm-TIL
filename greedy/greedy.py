
# n=1260
# count = 0
# #큰 단위 화폐부터 차례대로 확인
# array = [500,100,50,10]

# for coin in array:
#   count += n // coin #해당 화폐로 거슬러 줄 수 있는 동전 개수 세기
#   print('count', count)
#   n %= coin
#   print('n', n)
  
# print('count', count)


# #공백 기준 입력값 받기
# n, k = map(int,input().split())

# result = 0
# while True:
#   #n이 k로 나누어 떨어지는 수가 될 때까지 빼기
#   target = (n // k) *k
#   print(target,'target!!!!', n)
#   result += (n-target)
#   print(result,'result!')
#   n = target
#   print(n,'n!')
#   #n이 k보다 작을때 탈출
#   if(n < k):
#     break
#   #k로 나누기
#   result += 1
#   n //= k

# #마지막으로 남은 수에 대하여 1씩 빼기
# print('resultresultresult', result)
# print('nnnn', n)
# result += (n-1)
# print('result', result)


##### 입력값의 오른쪽으로 곱하거나 더해서 가장 큰 수를 출력
data = input('0~9')
result = int(data[0])

for i in range(1,len(data)):
  num = int(data[i])
  if num <= 1 or result <=1:
    result += num
  else :
    result *=num
print(result)
    
  