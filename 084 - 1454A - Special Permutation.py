no_of_test_cases = int(input())
while no_of_test_cases:
    no_of_test_cases -= 1
    n = int(input())
    data = list(range(1, n+1))
    temp = data[0]
    data.pop(0)
    data.append(temp)
    res = ""
    for element in data:
        res += str(element) + " "
    print(res)

