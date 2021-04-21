def c_plus_equal(a, b, n):
    count = 0
    while True:
        if a < b:
            a += b
            count += 1
        elif b < a:
            b += a
            count += 1
        else:
            a += b
            count += 1
        if a > n or b > n:
            break
    return count


if __name__ == '__main__':
    no_of_test_cases = int(input())
    for i in range(no_of_test_cases):
        a, b, n = map(int, input().split())
        count = c_plus_equal(a, b, n)
        print(count)
