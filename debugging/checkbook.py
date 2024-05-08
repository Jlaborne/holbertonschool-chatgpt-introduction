class Checkbook:
    def __init__(self):
        # Initialize balance to 0.0 when a Checkbook object is created
        self.balance = 0.0

    def deposit(self, amount):
        # Add the deposit amount to the balance
        self.balance += amount
        # Print a message confirming the deposit and showing the updated balance
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        # Check if there are sufficient funds in the account for the withdrawal
        if amount > self.balance:
            # Print a message if there are insufficient funds
            print("Insufficient funds to complete the withdrawal.")
        else:
            # Subtract the withdrawal amount from the balance
            self.balance -= amount
            # Print a message confirming the withdrawal and showing the updated balance
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        # Print the current balance
        print("Current Balance: ${:.2f}".format(self.balance))

def main():
    # Create a Checkbook object
    cb = Checkbook()
    while True:
        # Ask the user what action they want to perform
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ")
        # Check the user's input and perform the corresponding action
        if action.lower() == 'exit':
            # Exit the loop if the user wants to exit
            break
        elif action.lower() == 'deposit':
            # Ask the user for the deposit amount and call the deposit method
            amount = float(input("Enter the amount to deposit: $"))
            cb.deposit(amount)
        elif action.lower() == 'withdraw':
            # Ask the user for the withdrawal amount and call the withdraw method
            amount = float(input("Enter the amount to withdraw: $"))
            cb.withdraw(amount)
        elif action.lower() == 'balance':
            # Call the get_balance method to display the current balance
            cb.get_balance()
        else:
            # Print a message for invalid commands
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    # Call the main function when the script is executed
    main()
