# ATM machine project in Python | python projects

import time

print('================================')
print('ATM machine project in Python')
print('================================')

print('please insert tour CARD.')
time.sleep(5)

password=1234
pin=int(input('enter your atm pin:'))
balance=5000
if pin==password:
    while True:
        print("""
              1==balance
              2==withdraw balance
              3==deposit balance
              4==exit
        """)
        try:
            option=int(input('please enter your choise:'))
        except:
            print('please enter valid option.')

        if option==1:
            print(f"your current balance is {balance}.")

        if option==2:
            withdraw_amount=int(input('please enter withdraw amount:'))
            balance=balance-withdraw_amount
            print(f"{withdraw_amount} is debited from your account")
            print(f"your updated balance is {balance}")

        if option==3:
            deposite_amount=int(input('enter deposite amount:'))
            balance=balance+deposite_amount
            print(f"{deposite_amount} is credited to your account")
            print(f"your updated balance is {balance}")

        if option==4:
            print('do you want quit:')
            s=input('enter y/n:')
            if s=='y':
                break
            else:
                continue

else:
    print('wrong password,please try again!')


