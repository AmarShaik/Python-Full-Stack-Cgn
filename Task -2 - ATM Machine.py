#ATM Machine Task
while True:
    account = 10000
    card = input('insert the card')
    pwd = 1234
    if card == 'c':
        print("Welcome Amar")
        password = int(input('enter the password:'))
        if password == pwd:
            option = int(input('''choose an option- 1.balance enquiry
                                                    2.withdraw'''))
            if option == 1:
                print('your balance is', account)
            elif option == 2:
                money = int(input('enter money to withdraw'))
                balance = account - money
                print("remaining account balance is ", balance)
            else:
                print("Exited")
                break
        else:
            print("Invalid Password")
    else:
        print("Invalid card")
