# for-loop is used for iterables
# for-loop is a counted loop (fixed number of items)

# for item in iterable object:
#     <statement with item>

spaces = ""
for c in "Hello World!":
    print(f"{spaces}{c}")
    spaces = spaces + " "

# for index in range(start(opt), end, step(opt)):
#    <statement>
#
# start is included, end is excluded
#
for i in range(5):  # for i in range(end=5)
    print(i)   # 0 1 2 3 4

print()

for i in range(7, 15):  # start=7, end=15(exclude)
    print(i)   # 7, 8, 9, 10, 11, 12, 13, 14

print()

for i in range(100, 200, 30): # start=100, end=200, step=30
    print(i)   # 100, 130, 160, 190








