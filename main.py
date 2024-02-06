# W - Withdraw
# D - Deposit
# E - Extract
# Q - Quit
balance = 0.0
extract = ""

while True: 
    print('''Choose the desired option:
        W - Withdraw
        D - Deposit
        E - Extract
        Q - Quit ''')

    option = input()

    if (option == 'W' or option == 'w'):
        print("Withdraw")

    elif (option == 'D' or option == 'd'):
        deposit = float(input("How do you want to deposit?"))

        if deposit > 0:
            balance = balance + deposit
            print(f"Your current balance now is: {balance}")
            extract = extract + f"Deposit: {deposit}\n"
        else: 
            print("Error, the value have to bigger than 0")

    elif (option == 'E' or option == 'e'):
        print(extract)

    elif (option == 'Q' or option == 'q'):
        print("Quit")
        
    else: 
        print("Invalid Option")