total_money = int(input())
bills = [100, 20, 10, 5, 1]
bills_count = 0
for bill in bills:
    bills_count += total_money // bill
    total_money %= bill

#
# while total_money > 0:
#     if total_money >= 100:
#         bills_count += total_money // 100
#         total_money %= 100
#     elif 20 <= total_money < 100:
#         bills_count += total_money // 20
#         total_money %= 20
#     elif 10 <= total_money < 20:
#         bills_count += total_money // 10
#         total_money %= 10
#     elif 5 <= total_money < 10:
#         bills_count += total_money // 5
#         total_money %= 5
#     elif 1 <= total_money < 5:
#         bills_count += total_money // 1
#         total_money %= 1

print(bills_count)
