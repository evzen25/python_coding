def main():
    print(" Welcome to the email slicer ")
    print("")

    email_input = input("Input your email address: ")

    (username, domain) = email_input.split("@")
    (domain, extension) = domain.split(".")

    print("Username: ", username)
    print("Domain: ", domain)
    print("extension: ", extension)

while True:
    main_input = input("Input 'quit' to exit or any other key to continue: ")
    if main_input.lower() == "quit":
        print("Program ended")
        break
    else:
        main()