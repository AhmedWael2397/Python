import ClientsApp as C
import BankServer as B
import random

def MainMenu():
    print('Press 1 for creating a new customer:\nPress 2 for logging in as an existing customer: \nPress 3 for displaying number of customers:\nPress 4 for exit\n')
    user_input = C.Numbering()
    while (user_input <= 0 or user_input > 4):
        print("Invalid Input\t Please Try again\n")
        print('Press 1 for creating a new customer:\nPress 2 for logging in as an existing customer: \nPress 3 for displaying number of customers:\nPress 4 for exit\n')
        user_input = C.Numbering()
    return user_input


while (1):
    UserInput = MainMenu()
    if (UserInput == 1):  # Create User
        name = input('Please Enter your Name\n')
        phone = input('Please Enter your Mobile Number\n')
        print('Please Enter the amount that you will deposit')
        Deposit = C.Numbering()
        while (Deposit < 500 or Deposit <= 0):
            print('Sorry but minimum Amount to open an account is 500 EGP\n')
            Deposit = C.Numbering()
        print('Please Enter your desired Pin-Code')
        NewCode = input()
        while (len(NewCode) != 4):
            print('Sorry but PinCode must be 4 charachters\n')
            NewCode = input()
        AccountNo = random.randint(100000, 500000)
        Adress = input('Please Enter your desired payment adress\n')
        PaymentAdress = Adress+'@AmitBank'
        counter=0
        u2 = B.AmitBank.create_user(
            name, phone, Deposit, NewCode, AccountNo, PaymentAdress, counter)
        C.UsersData(u2)
        print('User Account Created successfuly\n Welcome to Amit Bank Mr: ',
              u2.name, '\n Your Account number is: ', u2.AccountNo, 'your payment adress is ', u2.PaymentAdress)

    elif (UserInput == 2):  # LOG IN
        print('Please Enter your Account Number: ')
        UserAccount = C.Numbering()
        if (B.AmitBank.AccountLogin(UserAccount)):
            print('Logged in \n')
            SecondInput = C.AccountMenu()
        else:
            print('Login Failed')

    elif (UserInput == 3):  # Display Number of Customers
        UC = B.AmitBank.UsersCount()
        print(f'Number of Users in Amit Bank is: {UC} Users')