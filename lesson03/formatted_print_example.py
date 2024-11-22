
# title = "{:40}"   # placeholder with 40 spaces
# title = "{:^40}"   # placeholder with 40 spaces, ^ center the string
title = "{:=^40}"   # placeholder with 40 spaces, ^ center the string, = to fill up gaps
row = "| {:10} | {:10} | ${:<9.2f} |"   # .2f means 2 decimal places

print(title.format("Sales"))   # print("{:40}".format("Sales")) -> print(f"{'sales':40}")
print(row.format("Apple", 20, 1.50))
print(row.format("Pear", 30, 2.70))
print(row.format("Orange", 50, 3.258985))
print("=" * 40)        # horizontal rule
