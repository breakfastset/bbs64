
numbers = [x for x in range(5)]
print(numbers)

even_numbers = [x for x in range(5) if x % 2 == 0]
print(even_numbers)

squares = [x ** 2 for x in range(5)]
print(squares)

even_squares = [x ** 2 for x in range(5) if x % 2 == 0]
print(even_squares)

binaries = ['x' if x % 2 == 0 else 'y' for x in range(5)]
print(binaries)

print()
scores = [78, 56, 43, 89, 98, 55, 68, 20, 77, 71]

passes = []
for score in scores:
    if score >= 50:
        passes.append(score)
print(f"Number of passes: {len(passes)}")

pass_count = len([x for x in scores if x >= 50])
print(f"Number of passes: {pass_count}")

pass_count = sum([1 if x >= 50 else 0 for x in scores])
print(f"Number of passes: {pass_count}")






