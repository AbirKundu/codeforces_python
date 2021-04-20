no_of_test_cases = int(input())
for i in range(no_of_test_cases):
    n = int(input())
    data = [2**j for j in range(1, n+1)]
    temp = (n - 2) // 2
    one = data[-1]
    other = sum(data)
    if temp > 0:
        for j in range(temp):
            one += data[j]
    other -= one
    print(abs(one - other))