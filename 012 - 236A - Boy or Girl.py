user_name = input()
distinct_user_name = ''.join(set(user_name))
if len(distinct_user_name)%2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")