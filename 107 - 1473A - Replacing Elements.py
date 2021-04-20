no_of_test_cases = int(input())
for i in range(no_of_test_cases):
    n, d = map(int, input().split())
    arr = list(map(int, input().split()))
    all_small = all([(True if ele <= d else False) for ele in arr])
    if all_small:
        print("YES")
    else:
        arr.sort()
        first = second = together = False
        if len(arr) >= 2:
            first = arr[0] <= d
            second = arr[1] <= d
            together = (arr[0] + arr[1]) <= d
        if first and second and together:
            print("YES")
        else:
            print("NO")
