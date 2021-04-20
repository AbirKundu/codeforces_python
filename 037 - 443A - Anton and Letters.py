letters = list(input().replace("{","").replace("}","").replace(" ","").split(","))
if letters[0] == '':
    print(0)
else:
    print(len(set(letters)))
