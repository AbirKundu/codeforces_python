import math
no_of_test_cases =int(input())
for i in range(no_of_test_cases):
    n, m = map(int, input().split())
    print(math.ceil((n*m)/2))