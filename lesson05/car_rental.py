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
    print("Construction in progress...")

def main():
    # 0. Set up of available cars
    available_car_count = read_availability()    # read from file

    # 1. Print menu and ask user for a choice - input
    choice = input(MENU)

    # 2. Process input  -> # 3. Output
    if choice == "1":
        print("1. Renting Car")
        available_car_count = rent_car(available_car_count)
    elif choice == "2":
        print("2. Returning Car")
        available_car_count = return_car(available_car_count)
    elif choice == "3":
        print("3. Terms and Conditions")
        read_terms_and_conditions()
    elif choice == "4":
        print("4. Quit")
        print("Bye bye")
    else:
        print("Wrong option entered!")

    # 4. Save available_car_count to file
    save_availability(available_car_count)
    print("~`~`~Thank you for patronizing minimal car Co~`~`~")

main()
