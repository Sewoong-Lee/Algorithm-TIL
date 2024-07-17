#피시방알바

N = int(input())
wantList = map(int, input().split())

arr=[];
i = 0

for want in wantList:
  if want in arr:
    i +=1
  else:
    arr.append(want)

print(i)