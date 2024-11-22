
in_file = open("poem.txt", "r")
# No man is an island

first_char = in_file.read(1)    # read 1 character
print(f"First Char: {first_char}")

next_three_chars = in_file.read(3)  # read 3 chars "o m"
print(f"Next 3 chars: {next_three_chars}")

rest_of_line = in_file.readline()   # read a line
print(f"Rest of 1st line: {rest_of_line}")

second_line = in_file.readline()   # read a line
print(f"Second line: {second_line}")

rest_of_poem = in_file.read()     # read everything else
print(f"Rest of poems: {rest_of_poem}")

in_file.close()   # release resources / file back to system
