
def print_pretty(title):
    print("=" * 40)
    print(f"| {title:^36} |")
    print("=" * 40)

def main():
    print("Hello")    # belongs to main()
    print("Bye")      # belongs to main()
    print_pretty("BBS64")
    # Call print_pretty() function, pass in argument "BBS64"
    # title parameter of print_pretty() will now hold "BBS64"
    print_pretty("I love Python")
    print_pretty("I love iPhone 16")

main()     # call the main() function. Start of program