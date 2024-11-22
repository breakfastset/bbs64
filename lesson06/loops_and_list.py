
numbers = [44, 55, 77, 33, 43, 23, 90, 20]

for i in range(len(numbers)):  # ranged loop
    print(f"{i}  =>  {numbers[i]}")


print()

for num in numbers:   # for each loop
    print(num)

print()

print(90 in numbers)   # True
print(555 in numbers)   # False

print()

sorted_numbers = sorted(numbers)  # sorted function
# numbers retains the original order,
# sorted_numbers is a sorted copy

print(sorted_numbers)
print(numbers)

numbers.sort()   # this will apply sort directly on numbers
print(numbers)  # original copy is now modified

numbers.sort(reverse=True)
print(numbers)  # Descending order





