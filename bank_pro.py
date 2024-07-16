def show_bal(balance):
    print("#######################")
    print(f"Your balance is ${balance}")
    print("#######################")

def deposit():
    print("#######################")
    try:
        amount=float(input("Enter the amount you want to deposit: "))
        if amount<0:
            print("Invalid amount")
            return 0
        else:
            return amount
    except ValueError:
        print("Please enter a valid number")
        return 0
    finally:
        print("#######################")
    
def withdraw(balance):
    print("#######################")
    try:
        amount=float(input("Enter the amount to be withdrawn: "))
        if amount>balance:
            print("Insuffiecent funds 🥲")
            return 0
        elif amount<0:
            print("Enter a valid amount greater than 0")
            return 0
        else:
            return amount
    except ValueError:
        print("Please enter a valid number")
        return 0
    finally:
        print("#######################")
        
    
def authenticate(user_db):
    print("######## Login ########")
    username=input("Enter your username: ")
    password=input("Enter your password: ")
    if username in user_db and user_db[username]==password:
        print("Login successful")
        print("#######################")
        return True
    else:
        print("Invalid username or password")
        print("#######################")
        return False
def main():
    user_db={'user1':'pass1','user2':'pass2'}
    if not authenticate(user_db):
        return
    balance=0
    is_running=True

    while is_running:
        print("#######################")
        print("Welcome to BankPro !")
        print("#######################")
        print("1.Show Balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Exit")
        print("#######################")
        choice=input("Enter your choice: ")
        if choice=="1":
            show_bal(balance)
        elif choice=="2":
            balance+= deposit()
        elif choice=="3":
         balance-= withdraw(balance)
        else:
            is_running=False
            print("Thank You!! Have a nice day 😇")

if __name__=='__main__':
    main()