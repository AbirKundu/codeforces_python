no_of_test_cases = int(input())
for i in range(no_of_test_cases):
    len_arr = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    temp = arr[0]
    count = 1
    for j in range(1, len_arr):
        if arr[j] == temp or arr[j] == temp+1:
            count += 1
            temp = arr[j]

    if count == len_arr:
        print("YES")
    else:
        print("NO")
