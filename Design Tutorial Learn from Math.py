def check_not_prime(num):
    for i in range(2, (num // 2) + 1):
        if (num % i) == 0:
            return True
    else:
        return False


if __name__ == "__main__":
    n = int(input())
    for i in range(4, n):
        other = n - i
        if check_not_prime(i) and check_not_prime(other):
            print(f"{i} {other}")
            break
