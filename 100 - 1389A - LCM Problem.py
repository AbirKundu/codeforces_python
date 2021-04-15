no_of_test_cases = int(input())
for i in range(no_of_test_cases):
    l, r = map(int, input().split())
    if l*2 <= r:
        print(f"{l} {l*2}")
    else:
        print("-1 -1")