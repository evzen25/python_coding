def main():
    print("This program converts Czech crowns to Euros")
    print()

    convert_to_euros = lambda czech_crowns: round(czech_crowns * 0.042, 2)

    while True:
        command = input("Enter amount in Czech crowns: ")

        if command == 'end':
            break

        czech_crowns = float(command)

        euros = convert_to_euros(czech_crowns)

        print("That is", euros, "euros.")

main()