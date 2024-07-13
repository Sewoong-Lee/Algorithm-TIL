#카우버거
B, C, D = map(int, input().split())
B_list = list(map(int, input().split()))
C_list = list(map(int, input().split()))
D_list = list(map(int, input().split()))

o_price = sum(B_list) + sum(C_list) + sum(D_list)

B_list.sort(reverse=True)
C_list.sort(reverse=True)
D_list.sort(reverse=True)

min_num = min(B, C, D)
d_price = 0
for i in range(min_num):
    d_price += B_list[i] * 0.9
    d_price += C_list[i] * 0.9
    d_price += D_list[i] * 0.9

d_price += sum(B_list[min_num:])
d_price += sum(C_list[min_num:])
d_price += sum(D_list[min_num:])

print(int(o_price))
print(int(d_price))
