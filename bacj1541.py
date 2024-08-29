#[그리디]잃어버린 괄호
N = input()
pa = N.split('-')

r = sum(map(int, pa[0].split('+')))

for p in pa[1:]:
    r -= sum(map(int, p.split('+')))

print(r)
