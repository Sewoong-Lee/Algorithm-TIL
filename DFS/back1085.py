#직사각형에서 탈출
x, y, w, h = map(int, input().split())

distance_left = x
distance_right = w - x
distance_bottom = y
distance_top = h - y

min = min(distance_left, distance_right, distance_bottom, distance_top)

print(min)
