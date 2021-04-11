no_of_test_cases = int(input())
for i in range(no_of_test_cases):
    n = int(input())
    temp = []
    res = ""
    data = list(map(int, input().split()))
    for element in data:
        if element not in temp:
            temp.append(element)
            res += str(element) + " "

    print(str(res))