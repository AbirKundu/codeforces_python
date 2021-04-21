def check_equal():
    n = int(input())
    strings = []
    flag = False
    for j in range(n):
        strings.extend(input())
    for ele in set(strings):
        count = strings.count(ele)
        if count % n != 0:
            flag = True
    if flag:
        return 'NO'
    else:
        return 'YES'


if __name__ == '__main__':
    no_of_test_cases = int(input())
    for i in range(no_of_test_cases):
        res = check_equal()
        print(res)
