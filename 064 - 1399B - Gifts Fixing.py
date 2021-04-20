no_of_test_cases = int(input())
for i in range(no_of_test_cases):
    no_of_gifts = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    res = 0
    for j in range(len(a)):
        temp_a = a[j] - min(a)
        temp_b = b[j] - min(b)
        res += max(temp_a, temp_b)
    print(res)