
hand_phones = ["iPhone 16", "Galaxy Fold 5", "Oppo Pro 12", "Pixel 9", "Xiaomi 15"]
#                 0              1              2               3           4
#                 -5             -4            -3              -2           -1

print(hand_phones[0])   # iPhone 16
print(hand_phones[-5])  # iPhone 16

print(hand_phones[-1])  # Xiaomi 15

print()
print(len(hand_phones))  # 5

# slicing (means take a copy/part copy of the original list)
print(hand_phones[:3])   # indexes 0, 1, 2
print(hand_phones[2:])   # 2, 3, 4 ['Oppo Pro 12', 'Pixel 9', 'Xiaomi 15']
print(hand_phones[1:3])  # indexes 1, 2 ['Galaxy Fold 5', 'Oppo Pro 12']
print(hand_phones[1:4:2])  # step is 2  ['Galaxy Fold 5', 'Pixel 9']

print(hand_phones[::-1])  # reverse the order
# hand_phones[start:end:step]
# start is inclusive, end is excluded

print()
hp_copy = hand_phones[:]   # copy of the original list
print(hp_copy)

hand_phones[-1] = "Sony"   # modify the last item in the list
print(hand_phones)

del hand_phones[1]   # remove item at position 1
print(hand_phones)

hand_phones.pop(1)   # remove item at position 1
print(hand_phones)

hand_phones.append("Huawei")  # add to the end
print(hand_phones)

hand_phones.insert(2, "LG")  # insert LG at position 2
print(hand_phones)

hand_phones.pop()   # remove the last item
print(hand_phones)

# print(hand_phones[4])   # IndexError, as there are 4 items 0, 1, 2, 3

