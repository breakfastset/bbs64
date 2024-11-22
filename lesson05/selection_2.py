# 3. if-elif....else
# multiple pathways but only 1 is executed.
score = 65
grade = "NA"
if 70 <= score <= 100:
    grade = "HD"
elif 60 <= score < 70:
    grade = "Distinction"
elif 50 <= score < 60:
    grade = "Credit"
elif 0 <= score < 50:
    grade = "Fail"

print(f"You got {grade}")

print()
# 4. nested if
age = 35
is_working = False

if age >= 65 and is_working:
    rebate = 400
elif age >= 65 and not is_working:
    rebate = 800
elif age < 65 and is_working:
    rebate = 200
elif age < 65 and not is_working:
    rebate = 500

print(f"You get ${rebate}")

if age >= 65:
    if is_working:
        rebate = 400
    else:
        rebate = 800
elif age < 65:
    if is_working:
        rebate = 200
    else:
        rebate = 500

print(f"You get ${rebate}")
