MENU = """Welcome to the minimal car-rental company.
1. Rent car
2. Return car
3. Read T&C
4. Quit
Please choose an option: """

def read_availability():
    """Read and return the number of cars available from database."""
    fleet = []
    in_file = open("vehicles.csv", "r")

    for line in in_file.readlines():
        car = line.split(",")   #    split the line
        car[-1] = int(car[-1])  #    convert the last item to int
        fleet.append(car)      #    append list to fleet

    in_file.close()
    return fleet


def save_availability(num_cars):
    """Save updated number of cars to the database."""
    out_file = open("cars.txt", "w")

    line = "{}".format(num_cars)
    print(line, file=out_file)  # automatically add newline

    out_file.close()


def display_cars(fleet):
    """Display the fleet in a formatted manner."""
    print('-' * 60)
    for i in range(len(fleet)):
        car = fleet[i]    # a list representing a car eg. ['Toyota', 'Sienta', 'A', 5]
        make = car[0]     # 'Toyota'
        model = car[1]    # 'Sienta'
        car_class = car[2]  # 'A'
        car_count = car[3]  # 5
        print(f"| {i:3} | {make:18} | {model:14} | {car_class:4} | {car_count:5} |")
    print('-' * 60)


def get_car_choice(fleet):
    """Get a valid car choice from the fleet."""
    choice = int(input("Please choose car: "))
    while choice < 0 or choice >= len(fleet):
        print(f" -- Wrong choice! Must be 0 to {len(fleet) - 1} only!")
        choice = int(input("Please choose car: "))

    return choice   # choice is bound to be valid.

def rent_car(fleet):
    """Determine if car(s) are available for renting and update available car count."""

    # 1. display available cars
    display_cars(fleet)

    # 2. get car choice
    car_choice = get_car_choice(fleet)

    # 3. update car count if required and inform user
    num_cars = fleet[car_choice][-1]
    if num_cars >= 1:
        fleet[car_choice][-1] = fleet[car_choice][-1] -  1   # decrease by 1
        print("Your car is available at check out.")
    else:
        print("Sorry, the model you requested is not available at the moment.")

    return fleet

def return_car(num_cars):
    """Return a car and increase the available car count accordingly."""
    num_cars = num_cars + 1
    print("Car returned. Thank you!")
    return num_cars

def read_terms_and_conditions():
    """Display Terms and Conditions to User before renting out."""
    in_file = open("terms.txt", "r")
    line_count = 1
    for line in in_file.readlines():
        print(line)
        if line_count % 10 == 0:   # after every 10 lines
            dummy = input("--++-- Enter for more --++--")
        line_count += 1

    in_file.close()

def main():
    # 0. Set up of available cars
    fleet = read_availability()    # read from file
    # print(fleet)   # debugging to see whether we achieved a list of cars

    # 1. Print menu and ask user for a choice - input
    choice = input(MENU)  # 1. init

    while choice != "4": # 2. while condition is True
        # 2. Process input  -> # 3. Output
        if choice == "1":  # 3. body of statements
            print("1. Renting Car")
            fleet = rent_car(fleet)
        elif choice == "2":
            print("2. Returning Car")
            # available_car_count = return_car(available_car_count)
        elif choice == "3":
            print("3. Terms and Conditions")
            read_terms_and_conditions()
        else:
            print("Wrong option entered!")

        choice = input(MENU)  # 4. ask again to update condition
    #
    # # 4. Save available_car_count to file
    # save_availability(available_car_count)
    print("~`~`~Thank you for patronizing minimal car Co~`~`~")

main()
