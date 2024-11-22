numbers = [44, 55, 77, 33, 43, 23, 90, 20]

# add 1 to each of the element of the list.

for num in numbers:   # num is copy of the element
    num = num + 1

print(numbers)

# use for in range() loop to modify

for i in range(len(numbers)):
    numbers[i] = numbers[i] + 1

print(numbers)