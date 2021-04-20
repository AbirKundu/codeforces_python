no_of_test_cases = int(input())

for i in range(no_of_test_cases):
    a, b = map(int, input().split())
    diff = b - a
    move = 0
    while abs(diff) > 0:
        if diff < 0:
            if abs(diff) % 2 == 0:
                move += 1
                diff -= diff
            else:
                move += 1
                diff -= 1
        else:
            if diff % 2 != 0:
                move += 1
                diff -= diff
            else:
                move += 1
                diff -= 1
    print(move)