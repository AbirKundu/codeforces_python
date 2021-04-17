def main():
    s = map(ord, input())

    res = 0
    curr = 0

    for x in s:
        if ord('a') <= x <= ord('z'):
            x -= ord('a')
            res += min(abs(x - curr), 26 - abs(x - curr))
            curr = x
        else:
            break

    print(res)


if __name__ == '__main__':
    main()