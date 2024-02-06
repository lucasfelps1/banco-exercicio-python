# W - Withdraw
# D - Deposit
# E - Extract
# Q - Quit
balance = 0.0
extract = ""
dailywd = 3;

while True: 
    print('''Choose the desired option:
        W - Withdraw
        D - Deposit
        E - Extract
        Q - Quit ''')

    option = input()

    if (option == 'W' or option == 'w'):
        withdraw = float(input("How much do you want to withdraw?"))

        if dailywd < 1:
            print("Daily withdrawal limit reached...")
        elif withdraw > 500:
            print("The withdraw has to be smaller than 500")
        elif withdraw > balance:
            print(f"The withdraw is bigger than the balance! The balance is {balance}")
        else:
            balance -= withdraw
            print(f"Your current balance now is: {balance}")
            extract = extract + f"Withdraw: {deposit}\n"
            dailywd -= 1

    elif (option == 'D' or option == 'd'):
        deposit = float(input("How much do you want to deposit?"))

        if deposit > 0:
            balance = balance + deposit
            print(f"Your current balance now is: {balance}")
            extract = extract + f"Deposit: {deposit}\n"
        else: 
            print("Error, the value have to bigger than 0")

    elif (option == 'E' or option == 'e'):
        print("Extract: ")
        print(extract)
        
    elif (option == 'Q' or option == 'q'):
        print("Quiting...")
        break
    else: 
        print("Invalid Option...")