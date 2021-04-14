no_of_test_cases = int(input())
while no_of_test_cases:
    no_of_test_cases -= 1
    count = 1
    w, h, n = map(int, input().split())
    while w % 2 == 0 or h % 2 == 0:
        if w % 2 == 0:
            w //= 2
            count *= 2
        elif h % 2 == 0:
            h //= 2
            count *= 2
    if count >= n:
        print("YES")
    else:
        print("NO")
