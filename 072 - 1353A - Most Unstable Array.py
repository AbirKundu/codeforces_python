no_of_test_cases = int(input())
for i in range(no_of_test_cases):
    n, m = map(int, input().split())
    print(min(2, n-1) * m)

