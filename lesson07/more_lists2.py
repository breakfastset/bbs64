
brands = ["honda", "suzuki", "yamaha", "toyota", "tesla"
          ,"honda", "yamaha", "mercedes", "bmw", "bmw",
          "yamaha"]


target = "yamaha"

# method 1: not so efficient
# while target in brands:
#     brands.remove(target)

# method 2: more efficient
target_count = brands.count(target)
for i in range(target_count):
    brands.remove(target)

print(brands)

print()

numbers = [1, 2, 3]
numbers = numbers * 3
print(numbers)

print()

scores = [78, 56, 43, 89, 98, 55, 68, 20, 77, 71]
highest = max(scores)
lowest = min(scores)
total = sum(scores)
average = total / len(scores)

print(f"Range   : {lowest} to {highest}")
print(f"Average : {average:.2f}")





