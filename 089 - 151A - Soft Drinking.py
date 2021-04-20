no_of_friends, no_of_bottles, drink_quantity, no_of_limes, lime_slices, salt_quantity, friend_need_drink, friend_need_salt = map(int, input().split())
toast_using_drink = (no_of_bottles * drink_quantity)//friend_need_drink
toast_using_lime = (no_of_limes * lime_slices)
toast_using_salt = salt_quantity // friend_need_salt
print(min(toast_using_drink, toast_using_lime, toast_using_salt)//no_of_friends)