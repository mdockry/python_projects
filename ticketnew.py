import sys
import os

TICKET_PRICE = 10
tickets_remaining = 100

def request_ticket_price():
    os.system('clear')
    while True:
        tickets_requested =input("How many tickets are you considering purchasing? Press 'N' to quit and return to main menu   ")
        try:
            tickets_requested = int(tickets_requested)
            if tickets_requested > tickets_remaining:
                raise ValueError("There are only {} tickets remaining.".format(tickets_remaining))
        except ValueError as err:
            print("An error has occured: {}, please try again.".format(err))
        else:
            total_cost = int(tickets_requested) * TICKET_PRICE
            print("\nThe total cost for the amount of tickets requested {} is ${}\n".format(tickets_requested, total_cost))
            user_action = input("Would you like to go back to the main menu? Enter Y for Yes or type any key to get another price.")
            if user_action.lower() == "y":
                main()
            else:
                continue

def purchase_ticket():
    os.system('clear')
    global tickets_remaining

    while tickets_remaining >= 1:
        number_of_tickets = input("\n>> How many tickets would you like to purchase today?   ")
        try:
            number_of_tickets = int(number_of_tickets)
            if number_of_tickets > tickets_remaining:
                raise ValueError("There are only {} tickets remaining.".format(tickets_remaining))
        except ValueError as err:
            print("An error has occured: {}, please try again.".format(err))
        else:
            cost = number_of_tickets * TICKET_PRICE
            print("Great! You have chosen {} tickets and your total comes to ${}".format(number_of_tickets, cost))
            confirmation= input("\nAre you sure you want to continue with the purchase? Press Y for yes or N for different amount   ")

            if confirmation.lower() == "y":
                print("Thank you for your purchase!")
                tickets_remaining -= int(number_of_tickets)
                user_action = input("Would you like to go back to the main menu? Enter Y for Yes or type any key to get another price.")
                if user_action.lower() == "y":
                    main()
                else:
                    continue

    print("Sorry we're currently sold out!")


def main():
    os.system('clear')
    print("*" * 70)
    print("Welcome to the ticket purchasing app")
    print("*" * 70)

    print("")
    print("")

    user_name = input("Please enter your name to begin:   ")
    print("\nHi, {}!".format(user_name) + " There is currently {} tickets remaining".format(tickets_remaining))

    print("")
    print("""
             Type 1 to get a price for the amount of tickets you wish to purchase
             Type 2 to purchase tickets
             Press any key other than 1 and 2 to exit

             """)

    userchoice = input("\nWhat would you like to do?   ")

    if userchoice == "1":
        request_ticket_price()
    elif userchoice == "2":
        purchase_ticket()
    else:
        sys.exit("Goodbye")


main()
