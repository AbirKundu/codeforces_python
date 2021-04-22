def string_similarity(n, string):
    res = ""
    i = 0
    while i < len(string):
        res += string[i]
        i += 2
    print(res)


if __name__ == '__main__':
    no_of_test_cases = int(input())
    for i in range(no_of_test_cases):
        n = int(input())
        string = input()
        string_similarity(n, string)
