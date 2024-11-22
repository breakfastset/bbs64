seatings = [
    ["Vi", "Jinx", "Ekko"],              # row 0
    ["Caitlyn", "Mel", "Jayce"],         # row 1
    ["Viktor", "Vander", "Silco"],       # row 2
    ["Ambessa", "Penny", "Peggy"]        # row 3
]    # col 0     col 1     col 2

print(seatings[2][1])   # 3rd row, 2nd column Vander
print(seatings[0][0])   # Vi
print(seatings[-1][-1]) # Peggy

print("=" * 50)

for row in range(len(seatings)):   # number of rows
    for col in range(len(seatings[row])):   # number of cols
        print(seatings[row][col])

print("=" * 50)
print()

for row in range(len(seatings)):   # number of rows
    # start of row
    for col in range(len(seatings[row])):   # number of cols
        print(f"{seatings[row][col]:10}", end="")
    print()
    print("-" * 30)
    # end of row


print("=" * 50)
print()
print("-" * 40)
for row in range(len(seatings)):   # number of rows
    # start of row
    print("|", end="")
    for col in range(len(seatings[row])):   # number of cols
        print(f" {seatings[row][col]:^10} |", end="")
    print()
    print("-" * 40)
    # end of row