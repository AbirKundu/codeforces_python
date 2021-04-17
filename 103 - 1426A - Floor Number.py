def main(no_of_test_cases):
    for i in range(no_of_test_cases):
        apartment_number, apartment_on_each_floor = map(int, input().split())
        floor = apartment_number - 2
        if floor > 0 and floor % apartment_on_each_floor != 0:
            floor = (floor // apartment_on_each_floor) + 2
        elif floor > 0 and floor % apartment_on_each_floor == 0:
            floor = (floor // apartment_on_each_floor) + 1
        else:
            floor = 1
        print(floor)


if __name__ == '__main__':
    no_of_test_cases = int(input())
    main(no_of_test_cases)
