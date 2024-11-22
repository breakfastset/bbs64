import random
# <1. initialisation>
# while <2. condition> is True:
#      <3. statement 1>
#       ...
#      <statement n>
#      <4. update condition> (eventually to false)
#
# Note: Used when number of repetitions are UNKNOWN
answer = random.randint(1, 10)
guess = int(input("Guess a number between 1 to 10: ")) # 1.

while guess < 1 or guess > 10:  # while 2. condition
    print("Please enter a valid number from 1 to 10!")   # 3. statement
    guess = int(input("Guess a number between 1 to 10: "))  # 4.


if guess == answer:
    print("You win!")
else:
    print(f"You lose! Answer is {answer}")

count = 0
while count < 10:
    print(count)
    count = count + 1