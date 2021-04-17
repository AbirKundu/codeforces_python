def main(no_of_test_cases):
    for i in range(no_of_test_cases):
        arr_len = int(input())
        arr = list(map(int, input().split()))
        new_arr = ""
        i = 0
        j = -1
        while arr_len > 0:
            if arr_len != 1:
                new_arr += str(arr[i]) + " "
                new_arr += str(arr[j]) + " "
                i += 1
                j -= 1
                arr_len -= 2
            else:
                new_arr += str(arr[i]) + " "
                arr_len -= 1
        print(new_arr)


if __name__ == '__main__':
    no_of_test_cases = int(input())
    main(no_of_test_cases)
