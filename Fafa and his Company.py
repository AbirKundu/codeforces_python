no_of_employee = int(input())
count = 0
if no_of_employee == 1:
    print(1)
else:
    for i in range(1, no_of_employee):
        if (no_of_employee - i) % i == 0:
            count += 1

    print(count)