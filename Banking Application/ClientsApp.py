
import os
import shutil
from BankServer import AmitBank

directory = '.\\Bank Customers'
if os.path.exists(directory):
    shutil.rmtree(directory)

os.mkdir(directory)

def Numbering():
    num = int(input())
    return num

def UsersData(obj):
    path = os.path.join(directory, obj.name)
    if not os.path.exists(path):
        os.mkdir(path)
    NewDir = path+'\\Info.txt'
    file = open(NewDir, 'w')
    file.write(f'Name: {obj.name}\nMobile Number: {obj.MobileNo}\nBalance: {obj.initalAmount}\nAccount Number: {obj.AccountNo}\nPayment Address: {obj.PaymentAdress}\n')
    file.close()


def Transactioncounter(obj, type, amount):
    path = os.path.join(directory, obj.name)
    if not os.path.exists(path):
        os.mkdir(path)
    NewDir = path+'\\Transactions.txt'
    file = open(NewDir, 'a+')
    file.write(f'-Transaction number {obj.counter}:\t{type}\t\t{amount}\t\n\n')
    file.close()


def AccountMenu():

    u1 = AmitBank.status()
    print('Press 1 for Deposit:\nPress 2 for Withdrawl: \nPress 3 for money transfer:\nPress 4 to log out\n')
    AccountInp = Numbering()
    while (AccountInp <= 0 or AccountInp > 4):
        print("Invalid Input\t Please Try again\n")
        print('Press 1 for Deposit:\nPress 2 for Withdrawl: \nPress 3 for money transfer:\nPress 4 to log out\n')
        AccountInp = Numbering()
    while (AccountInp != 4):
        AmitBank.status()
        ############### DEPOSITING MONEY ####################
        if (AccountInp == 1):
            print('Enter your deposited amount\n')
            DepositAmount = Numbering()
            u1.initalAmount += DepositAmount
            print(f'New Balance: {u1.initalAmount}')
            UsersData(u1)
            u1.counter += 1
            Transactioncounter(u1, 'Deposit', DepositAmount)
            print('Press 1 for Deposit:\nPress 2 for Withdrawl: \nPress 3 for money transfer:\nPress 4 to log out\n')
            AccountInp = Numbering()

        ############### WITHDRAWING MONEY ####################
        elif (AccountInp == 2):
            print('Enter Amount to Withdraw\n')
            WithdrawAmount = Numbering()
            if (u1.initalAmount < WithdrawAmount):
                print('amount is not available in your account\n')
                print(f'your current balance is: {u1.initalAmount}')
                print(
                    'Press 1 for Deposit:\nPress 2 for Withdrawl: \nPress 3 for money transfer:\nPress 4 to log out\n')
                AccountInp = Numbering()
            else:
                print('Transaction processing\n')
                u1.initalAmount -= WithdrawAmount
                print(f'your new balance is: {u1.initalAmount}')
                UsersData(u1)
                u1.counter += 1
                Transactioncounter(u1, 'Withdrawl', WithdrawAmount)
                print(
                    'Press 1 for Deposit:\nPress 2 for Withdrawl: \nPress 3 for money transfer:\nPress 4 to log out\n')
                AccountInp = Numbering()
        ################# TRANSFERING MONEY ##################
        else:
            RecpAdress = input('Please Enter the receipent payment adress\n')
            bankadress = '@AmitBank'
            RecpPaymentAdress = RecpAdress+bankadress
            print('Enter Transferred amount\n')
            TransAmount = Numbering()
            AmitBank.transfer(RecpPaymentAdress, TransAmount)
            print('Press 1 for Deposit:\nPress 2 for Withdrawl: \nPress 3 for money transfer:\nPress 4 to log out\n')
            AccountInp = Numbering()
    print('\n Logging Out\n')
    return
