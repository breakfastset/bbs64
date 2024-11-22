
lecturer_count = 1
student_count = 22
room = "501"

total_count = lecturer_count + student_count

# Desired output
# There are 23 people in room 501.

# 1. print using commas (comma will add an extra space before and after)
print("There are", total_count, "people in room", room, ".")

# 2. print using '+' -> string concatenation
print("There are " + str(total_count) + " people in room " + room + ".")

# 3. print using .format() method
print("There are {} people in room {}.".format(total_count, room))

# 4. print using f""
print(f"There are {total_count} people in room {room}.")