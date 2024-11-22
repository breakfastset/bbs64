from sys import argv   # from library sys import argument vector

if len(argv) >= 3:     # if number of arguments are 3 or more
    print(f"argv[0]: {argv[0]}")   # Program file
    print(f"argv[1]: {argv[1]}")   # from command line
    print(f"argv[2]: {argv[2]}")   # from command line

print("End of program.")