no_of_layers_of_love_and_hate = int(input())
feelings = ['I hate', 'it']
if no_of_layers_of_love_and_hate == 1:
    print(' '.join(feelings))
else:
    for i in range(1, no_of_layers_of_love_and_hate):
        if i % 2 != 0:
            feelings.insert(-1, "that I love")
        else:
            feelings.insert(-1, "that I hate")
    print(' '.join(feelings))