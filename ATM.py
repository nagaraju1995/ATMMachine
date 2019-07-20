data = {'Venkatesh' : {
         'password':[1234],
         'balance':[2000]
},
'Manasa' : {
        'password': [5678],
        'balance': [4000]
}}

name = input("Enter the name")
for i in data:
    if i == name:
        chance = 3
        while chance>0:
            code = int(input("Enter the password"))
            if code == data[name]['password'][-1]:
                print("Press 1 for checking the balance")
                print("press 2 for withdrawing")
                print("press 3 for depositing the money")
                print("press 4 to change password")
                option = input("Enter the option")
                if option == '1':
                    bal = data[name]['balance'][-1]
                    print("Your current balance is :",bal)
                    break
                if option == '2':
                    bal = data[name]['balance'][-1]
                    withdraw = int(input("Enter the amount"))
                    if withdraw > bal:
                        print("Insufficient balance")
                        break
                    else:
                        bal = bal - withdraw
                        print("Amount withdrawn:", withdraw)
                        print("Your current balance is:",bal)
                        break
                if option == '3':
                    bal = data[name]['balance'][-1]
                    deposit = int(input("Enter the amount"))
                    bal = bal + deposit
                    print("Amount deposited:", deposit)
                    print("Your current balance is:", bal)
                    break
                if option == '4':
                    new_password = input("Enter the new password")
                    if (len(new_password) < 4) | (len(new_password) > 4):
                        print("Password length should be 4")
                        break
                    else:
                        password = new_password
                        print("New Password is", new_password)
                        break
            else:
                chance -=1
                if chance == 0:
                    raise AssertionError("Account is blocked")
                    break
        else:
            print("User doesnt exists")
            break