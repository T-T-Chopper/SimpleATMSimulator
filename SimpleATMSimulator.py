print("Welcome to the Simple ATM Simulator!")

balance = 1000  # initial balance
user_pin = int(1234)  # correct PIN value

entered_pin = int(input("Please enter your pin: "))

# Loop until user enters the correct PIN
while entered_pin != 1234:
    atm_on = False
    entered_pin = int(input("Wrong pin please enter pin correctly: "))

print() 

# When correct PIN is entered, turn ATM on
if user_pin == entered_pin:
    atm_on = True

# Main ATM menu loop
while atm_on:
    print("Press 1 to check balance")
    print("Press 2 to deposit money")
    print("Press 3 to withdraw money")
    print("Press 4 to Exit")
    print() 

    user_choise = int(input("Enter your choice: "))
    print() 

    # Option 1: Check balance
    if user_choise == 1:
        print("Your balance is ", balance)
        print()

    # Option 2: Deposit money
    elif user_choise == 2:
        deposit = int(input("Please enter deposit amount: "))
        print()
        balance = deposit + balance  # add deposit to balance
        print("Deposit is successful, your new balance is :", balance)
        print() 

    # Option 3: Withdraw money
    elif user_choise == 3:
        withdraw = int(input("Please enter withdrawal amount: "))
        print() 
        # Check if balance is enough
        if balance < withdraw:
            print("Balance is insufficient, please enter a correct amount.")
            print() 
        else:
            balance = balance - withdraw  # subtract money

    # Option 4: Exit ATM
    elif user_choise == 4:
        print("HAVE A NICE DAY.")
        atm_on = False  # turn ATM off

    # If user enters an invalid number
    else:
        print("Please enter a valid number, try again")
        print() 
