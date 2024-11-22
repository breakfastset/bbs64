# AND
# -> all conditions must be True to be True
# -> if one condition is False,
#    the rest of the conditions will not be processed (short-circuit)
temperature = 28
is_rainy = True

# if temperature is less than 30 and is_rainy == False
if temperature < 30 and is_rainy == False:
    print("Time for a Hike!")
else:
    print("Wait for a better weather!")

# OR
# -> at least one condition must be True to be True
# -> if one condition is True,
#    the rest of the conditions will not be processed (short-circuit)
beverage = "coffee"

if beverage == "coffee" or beverage == "tea":
    print("It's going to be a good morning")
else:
    print("No thanks")

# NOT
# -> flip the condition
#    eg. while not valid_input:   # while valid_input == False:
#    eg. if graduated:    # if graduated == True:
is_happy = True
if not is_happy:    # if is_happy == False:
    print("Here's a chocolate drink to make you happy")
else:
    print("Buy me a drink")

is_happy = not is_happy
print(f"Value of is_happy {is_happy}")
