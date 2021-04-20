no_of_test_cases = int(input())
for i in range(no_of_test_cases):
    test_case = int(input())
    count = 0
    round_number = ""
    while test_case > 0:
        if test_case in range(1,11):
            count += 1
            round_number += str(test_case) + " "
            test_case = 0
        else:
            div_value = 10
            count += 1
            div_value = div_value ** (len(str(test_case)) - 1)
            data = int(str(test_case)[0]) * div_value
            test_case -= data
            round_number += str(data) + " "
    print(count)
    print(round_number)





