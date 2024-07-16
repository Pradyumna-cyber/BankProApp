# BankProApp

The provided code is a simple banking application in Python that allows users to authenticate, check their balance, deposit money, and withdraw money. Here is a detailed explanation of how the code works:

### Functions

1. **show_bal(balance)**
   - **Purpose:** Displays the current balance.
   - **Input:** `balance` - the current balance.
   - **Output:** Prints the balance enclosed in decorative lines.

2. **deposit()**
   - **Purpose:** Prompts the user to enter an amount to deposit.
   - **Output:** Returns the deposited amount if valid, otherwise returns 0.
   - **Process:**
     - Asks the user for an amount to deposit.
     - Checks if the amount is valid (greater than 0).
     - Handles invalid input (non-numeric or negative numbers) by catching `ValueError`.

3. **withdraw(balance)**
   - **Purpose:** Prompts the user to enter an amount to withdraw.
   - **Input:** `balance` - the current balance.
   - **Output:** Returns the withdrawn amount if valid, otherwise returns 0.
   - **Process:**
     - Asks the user for an amount to withdraw.
     - Checks if the amount is valid (greater than 0 and less than or equal to the current balance).
     - Handles invalid input (non-numeric or negative numbers) by catching `ValueError`.

4. **authenticate(user_db)**
   - **Purpose:** Authenticates the user based on a predefined username and password dictionary.
   - **Input:** `user_db` - a dictionary containing usernames and passwords.
   - **Output:** Returns `True` if authentication is successful, otherwise returns `False`.
   - **Process:**
     - Prompts the user for a username and password.
     - Checks if the provided credentials match any entry in the `user_db`.

### Main Program

1. **main()**
   - **Purpose:** The main function that drives the banking application.
   - **Process:**
     - Defines a user database `user_db` with predefined usernames and passwords.
     - Calls `authenticate(user_db)` to authenticate the user. If authentication fails, the program exits.
     - Initializes `balance` to 0.
     - Runs a loop (`is_running=True`) to continuously prompt the user for actions until they choose to exit.
     - Displays a menu with options to show balance, deposit, withdraw, or exit.
     - Based on the user's choice, calls the appropriate function (`show_bal`, `deposit`, or `withdraw`) and updates the balance accordingly.
     - Exits the loop and prints a goodbye message when the user chooses to exit.

### Example Execution

1. The program starts and prompts the user to log in.
2. Once logged in, it displays a menu with options to show balance, deposit, withdraw, or exit.
3. Depending on the user's choice:
   - `1` shows the current balance.
   - `2` prompts the user to enter an amount to deposit and updates the balance.
   - `3` prompts the user to enter an amount to withdraw and updates the balance if there are sufficient funds.
   - Any other input exits the program with a thank-you message.

### Conclusion

This code is a simple simulation of a banking system with basic functionalities such as authentication, balance inquiry, deposit, and withdrawal. It uses basic control structures like loops, conditionals, and exception handling to provide a user-friendly interaction.


###Screenshots:
1. <img width="425" alt="image" src="https://github.com/user-attachments/assets/c452e92b-6610-44b3-9d7a-be56a12410ca">
2. <img width="374" alt="image" src="https://github.com/user-attachments/assets/3d49eb31-4f36-4cae-9ddc-add2cb437d5c">
3. <img width="412" alt="image" src="https://github.com/user-attachments/assets/d379cb61-8648-4b8d-a8a6-bdeeeb608a7b">
4. <img width="376" alt="image" src="https://github.com/user-attachments/assets/8987e6ef-af57-4f59-94e6-a1b9a5dad5af">
5. <img width="503" alt="image" src="https://github.com/user-attachments/assets/94e0196c-405f-4045-961f-f6813814c573">
6.<img width="589" alt="image" src="https://github.com/user-attachments/assets/3173e265-bd20-496a-822d-487601cd0468">







