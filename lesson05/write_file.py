
lines = ["this is a line", "second line", "third line", "fourth line"]

out_file = open("test.txt", "w")

for line in lines:
    print(line, file=out_file)

out_file.close()