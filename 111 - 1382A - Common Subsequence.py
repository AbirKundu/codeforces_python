def common_subsequence(n, m):
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    elements = set(arr1) & set(arr2)
    if len(elements) > 0:
        print("YES")
        print(f"1 {list(elements)[0]}")
    else:
        print("NO")


if __name__ == '__main__':
    no_of_test_cases = int(input())
    for i in range(no_of_test_cases):
        n, m = map(int, input().split())
        common_subsequence(n, m)
