no_of_test_cases = int(input())
for i in range(no_of_test_cases):
    arr_len = int(input())
    arr = list(set(map(int, input().split())))
    arr.sort()
    print(len(arr))