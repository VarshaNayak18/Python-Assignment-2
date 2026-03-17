# Question 10: Simple ATM Simulator
"""
Create an ATM simulation with initial balance = ₹10,000.
Menu: 1. Check Balance 2. Deposit Money 3. Withdraw Money 4. Exit
Rules:
- Check sufficient balance before withdrawal
- Minimum balance of ₹500 must remain at all times
- Display transaction messages and updated balance after each transaction
"""

# Initial Balance
balance = 10000

while True:
    print("ATM SIMULATOR")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")
    # Take user input of choice
    choice = input("Enter your choice: ")

    if choice == "1":
        print(f"Balance: {balance}")
    
    elif choice == "2":
        deposit = int(input("Enter amount to deposit: "))
        print("Deposit successful!")
        balance += deposit
        print(f"New balance: {balance}")
    
    elif choice == "3":
        withdrawal = int(input("Enter amount to withdraw: "))
        if (balance - withdrawal) >= 500:
            balance -= withdrawal
            print("Withdrawal successful!")
            print(f"New balance: {balance}")
        else:
           print("Withdrawal NOT successful, as account should have minimum balance of ₹500") 
           print(f"Amount available for withdrawal: {balance - 500}")
    
    elif choice == "4":
        print("Exiting program")
        break

    else:
        print("Invalid Choice")