no_of_test_cases = int(input())
for i in range(no_of_test_cases):
    result = ""
    test_case = input()
    result += test_case[0]
    for i in range(1,len(test_case)):
       if i % 2 != 0:
           result += test_case[i]

    print(result)

