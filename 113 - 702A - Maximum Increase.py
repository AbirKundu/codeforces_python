def maximum_increase(n, arr):
    count = 0
    c_lst = []
    temp = arr[0]
    for i in range(1, len(arr)):
        max_item = max(temp, arr[i])
        if max_item != temp:
            count += 1
            temp = max_item
        else:
            temp = arr[i]
            c_lst.append(count+1)
            count = 0
        if i == len(arr) - 1:
            c_lst.append(count+1)
    if len(c_lst) > 0:
        print(max(c_lst))
    else:
        print(1)


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    maximum_increase(n, arr)