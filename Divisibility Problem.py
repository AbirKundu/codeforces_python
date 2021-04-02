no_of_test_cases = int(input())

for i in range(no_of_test_cases):
    a, b = map(int, input().split())
    if a % b != 0:
        print(b - (a % b))
    else:
        print(0)
