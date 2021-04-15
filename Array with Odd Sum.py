no_of_test_cases = int(input())
for i in range(no_of_test_cases):
    len_arr = int(input())
    arr = list(map(int, input().split()))
    check_all_element_even = all(i % 2 == 0 for i in arr)
    check_all_element_odd = all(i % 2 != 0 for i in arr)
    if check_all_element_even or (check_all_element_odd and sum(arr) % 2 == 0):
        print("NO")
    else:
        print("YES")
