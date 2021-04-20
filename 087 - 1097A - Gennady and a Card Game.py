on_table_card = input()
in_hand_card = input().split()
flag = False
for card in in_hand_card:
    if card[0] == on_table_card[0] or card[1] == on_table_card[1]:
        flag = True

if flag:
    print("YES")
else:
    print("NO")
