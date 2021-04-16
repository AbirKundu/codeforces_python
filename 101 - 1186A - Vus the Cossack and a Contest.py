no_of_participant, no_of_pens, no_of_notebooks = map(int, input().split())
if no_of_pens >= no_of_participant and no_of_notebooks >= no_of_participant:
    print("YES")
else:
    print("NO")
