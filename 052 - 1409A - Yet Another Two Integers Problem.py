no_of_test_cases = int(input())
for i in range(no_of_test_cases):
    a, b = map(int, input().split())
    diff = abs(a - b)
    print((diff + 9) // 10)
