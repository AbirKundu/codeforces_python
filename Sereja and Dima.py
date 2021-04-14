no_of_card_on_table = int(input())
cards_value = list(map(int, input().split()))
sareja = dima = 0
while len(cards_value) > 0:
    sareja += max(cards_value[0], cards_value[-1])
    cards_value.remove(max(cards_value[0], cards_value[-1]))
    if len(cards_value) > 0:
        dima += max(cards_value[0], cards_value[-1])
        cards_value.remove(max(cards_value[0], cards_value[-1]))

print(f"{sareja} {dima}")
