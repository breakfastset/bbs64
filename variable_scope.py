
name = "Koala"  # global

def useless_function():
    print("inside function")
    print(name)   # global var
    # print(her_name)    # her_name is local to main()

def main():
    her_name = "Powder"  # local
    print(name)     # printing global var
    print(her_name) # printing local var

    useless_function()

main()
