no_of_test_cases = int(input())
for i in range(no_of_test_cases):
    a,b,c,n = map(int, input().split())
    max_value = max(a,b,c)
    rem = (max_value - a) + (max_value - b) + (max_value - c)
    left = n - rem
    if left >= 0 and left % 3 == 0:
        print("YES")
    else:
        print("NO")