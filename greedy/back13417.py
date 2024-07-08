#카드 문자열
T = int(input().strip())
for _ in range(T):
    N = int(input().strip())
    cards = input().strip().split()
    result = []
    for card in cards:
        if not result:
            result.append(card)
        else:
            if card + ''.join(result) < ''.join(result) + card:
                result.insert(0, card)
            else:
                result.append(card)
    print(''.join(result))