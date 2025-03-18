print("Welcome to Simple ATM Simulator!")
print("Menu:")
print("1. Check Balance")
print('2. Deposit Money')
print('3. Withdraw Money')
print('4. Exit')

balance=1000.00
deposit=0.00
withdraw=0.00




input_num=float(input("Enter the number of your choice: "))
while(input_num== 1 or 2 or 3):
    if(input_num==1):
        print("Your current balance is: $", format(balance,'.2f'))
        input_num=float(input("Enter new number of choice: "))
    elif(input_num==2):
        newdeposit=float(input("Enter the amount to deposit: $"))
        balance=(float(deposit+balance+newdeposit))
        print("Deposit successful! Your new balance is: $",format(balance,'.2f'))
        input_num=float(input("Enter new number of choice: "))
    elif(input_num==3):
        newwithdraw=float(input("Enter the amount to withdraw: $"))
        if(newwithdraw>balance):
            print("Insufficient funds.")
        else:
            balance=(float(balance-newwithdraw))
            print("Withdrawal successful! Your new balance is: $",format(balance,'.2f'))
            input_num=float(input("Enter new number of choice: "))
    else:
        print("Thank you for using the ATM. Goodbye!")
        break

