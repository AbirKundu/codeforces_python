no_of_test_cases = int(input())
for i in range(no_of_test_cases):
    n, k = map(int,  input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    for i in range(n):
        if k == 0:
            break
        else:
            max_b = max(b)
            min_a = min(a)
            if max_b > min_a:
                a.append(max_b)
                a.remove(min_a)
                b.append(min_a)
                b.remove(max_b)
            k -= 1

    print(sum(a))
