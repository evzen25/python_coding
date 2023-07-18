
def is_leap_year(year):
    print("This is the leap year checker, welcome!\n")
    
    while True:
        command = input("Type the year or 'end' to exit: ")
    
        if command == "end":
            break 

        year = int(command)
        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    print("Leap Year")
                else:
                    print("Not leap year")
            else:
                print("Leap year")
        else:
            print("Not leap year")

is_leap_year(2020)







