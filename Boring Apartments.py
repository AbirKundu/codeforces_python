no_of_test_cases = int(input())
for i in range(no_of_test_cases):
    no_of_apartment = int(input())
    cnt = 0
    if no_of_apartment % 2 == 0:
        floor = (int(str(no_of_apartment)[0]) // 2) * 2
    else:
        floor = (int(str(no_of_apartment)[0]) // 2) + ((int(str(no_of_apartment)[0]) // 2) + 1)
    cnt = (floor-1) * 10 + sum(range(1,str(no_of_apartment).count(str(floor))+1))
    print(cnt)