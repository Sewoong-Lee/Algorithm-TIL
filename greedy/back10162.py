#전자레인지
Abtn = 300
Bbtn = 60
Cbtn = 10

T = int(input())

A_count = T//Abtn
T %= Abtn
B_count = T//Bbtn
T %= Bbtn
C_count = T//Cbtn
T %= Cbtn
if T != 0:
  print(-1)
else:
  print(A_count,B_count,C_count)