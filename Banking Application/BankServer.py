import ClientsApp as C


# con= psycopg2.connect(
#   database = 'Bank',
#  user = 'postgres',
#    password = '2397'
#    host = 'localhost'
#    port = '5432'
#)
#cursor_obj=con.cursor

class User:
    def __init__(self, name = '', MobileNo = '', initalAmount = 0, PIN = '', AccountNo = 0, PaymentAdress = '', counter = 0):
        self.name=name
        self.MobileNo=MobileNo
        self.initalAmount=initalAmount
        self.PIN=PIN
        self.AccountNo=AccountNo
        self.PaymentAdress=PaymentAdress
        self.counter=counter


class Bank:
    def __init__(self):
        self.users=[]
        self.CurrentUser=User()
        self.ReceivingUser=User()

    def create_user(self, name, MobileNo, initalAmount, PIN, AccountNo, paymentAdress, counter = 0):
        user=User(name, MobileNo, initalAmount,
                    PIN, AccountNo, paymentAdress, counter)
        self.users.append(user)
        return user

    def AccountLogin(self, Account):
        for user in self.users:
            if (user.AccountNo == Account):
                print('Welcome MR: ', user.name, '\n')
                print('Please enter your secret pin')
                # print(user.PIN)
                # print(type(user.PIN))
                pin=input()
                # print(pin)
                # print(type(pin))
                for i in range(3):
                    if user.PIN == pin:
                        self.CurrentUser=user
                        return True
                    else:
                        print('Invalid Pin , Try Again')
                        pin=input()
                print('Maximum number of trials Exceeded , Logging out \n')
                return False

        print('Account Not found\n')

    def status(self):
        print(f'User: {self.CurrentUser.name} \t AccountNo: {self.CurrentUser.AccountNo} \t Balance: {self.CurrentUser.initalAmount} EGP')
        return self.CurrentUser

    def transfer(self, RecPaymentAdress, amount):
        if (self.CurrentUser.initalAmount <= amount+500):  # ACCOUNT MUST CONTAIN AT LEAST 500 EGP
            print('Cannot Proceed \n Amount unavailable in your account')
        else:
            for user in self.users:
                if (user.PaymentAdress == RecPaymentAdress):
                    self.ReceivingUser=user
                    if (self.CurrentUser.PaymentAdress == RecPaymentAdress):
                        print('Cannot Transfer money to your own account\n')
                        return
                    else:
                        print(
                            'Enter your secret pin to confirm Transaction request:\t')
                        pcode=input()
                        if (pcode == self.CurrentUser.PIN):
                            self.CurrentUser.initalAmount -= amount
                            self.ReceivingUser.initalAmount += amount
                            print('Trasnfer Complete')
                            C.UsersData(self.CurrentUser)
                            self.CurrentUser.counter += 1
                            C.Transactioncounter(
                                self.CurrentUser, 'Transferred', amount)
                            C.UsersData(self.ReceivingUser)
                            self.ReceivingUser.counter += 1
                            C.Transactioncounter(
                                self.ReceivingUser, 'Received', amount)
                            AmitBank.status()
                            return

                        else:
                            print('Transfer failed')
                            return

            print('provided payment adress is invalid \n')

    def UsersCount(self):
        count=len(self.users)
        return count

AmitBank=Bank()
