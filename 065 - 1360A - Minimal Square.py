no_of_test_cases = int(input())
for i in range(no_of_test_cases):
    l, b = map(int, input().split())
    print((min(max(2 * b, l), max(2 * l, b))) ** 2)
