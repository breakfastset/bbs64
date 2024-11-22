money_in = int(input("How much income? "))
money_out = int(input("Expenses? "))
savings = money_in - money_out

out_file = open("savings.txt", "a")
# w is for overwrite, a is for appending

line = f"Savings: ${savings}"  # Savings: $55.99
out_file.write(line + "\n")

out_file.close()