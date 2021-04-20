no_of_char = int(input())
word = input()
if len(set(word.lower())) >= 26:
    print("YES")
else:
    print("NO")