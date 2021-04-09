no_of_test_cases = int(input())
for i in range(no_of_test_cases):
    len_array = int(input())
    arr = list(map(int, input().split()))
    odd = even = 0
    for j in range(len_array):
        if j % 2 != arr[j] % 2:
            if j % 2 == 0:
                even += 1
            else:
                odd += 1

    if even == odd:
        print(even)
    else:
        print(-1)
