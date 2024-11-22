MENU = """Welcome to the minimal car-rental company.
1. Rent car
2. Return car
3. Read T&C
4. Quit
Please choose an option: """

def read_availability():
    """Read and return the number of cars available from database."""
    num_cars = 0
    in_file = open("cars.txt", "r")

    line = in_file.readline()
    num_cars = int(line)    # convert to integer

    in_file.close()
    return num_cars


def save_availability(num_cars):
    """Save updated number of cars to the database."""
    out_file = open("cars.txt", "w")

    line = "{}".format(num_cars)
    print(line, file=out_file)  # automatically add newline

    out_file.close()

def rent_car(num_cars):
    """Determine if car(s) are available for renting and update available car count."""
    if num_cars > 0:
        num_cars = num_cars - 1
        print("Your car is available at checkout.")
    else:
        print("Sorry, but no cars available at the moment.")

    return num_cars

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
    available_car_count = read_availability()    # read from file

    # 1. Print menu and ask user for a choice - input
    choice = input(MENU)  # 1. init

    while choice != "4": # 2. while condition is True
        # 2. Process input  -> # 3. Output
        if choice == "1":  # 3. body of statements
            print("1. Renting Car")
            available_car_count = rent_car(available_car_count)
        elif choice == "2":
            print("2. Returning Car")
            available_car_count = return_car(available_car_count)
        elif choice == "3":
            print("3. Terms and Conditions")
            read_terms_and_conditions()
        else:
            print("Wrong option entered!")

        choice = input(MENU)  # 4. ask again to update condition

    # 4. Save available_car_count to file
    save_availability(available_car_count)
    print("~`~`~Thank you for patronizing minimal car Co~`~`~")

main()
