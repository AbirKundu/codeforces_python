guest_name = input()
resident_host = input()
pile_letters = input()
count = 0
guest_and_resident_name_together = guest_name+resident_host
guest_and_resident_letters_dict = {}
pile_letters_dict = {}
for char in guest_and_resident_name_together:
    guest_and_resident_letters_dict[char] = guest_and_resident_name_together.count(char)

for char in pile_letters:
    pile_letters_dict[char] = pile_letters.count(char)

if guest_and_resident_letters_dict == pile_letters_dict:
    print("YES")
else:
    print("NO")