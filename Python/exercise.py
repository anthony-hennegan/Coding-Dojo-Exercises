
print("")
print("Exercise 1")
print("====================")
print("")

password = "python123"

while True:
    password_response = input("Enter a password: ")
    if password_response == password:
        print("Access granted.")
        break
    else:
        print("Incorrect password. Try again.")

print("")
print("Exercise 2")
print("====================")
print("")

while True:
    number_response = input("Enter a number: ")
    
    try:
        number = int(number_response.strip())
        
        if number >= 0:
            print("Accepted")
            break
        else:
            print("Number must be greater than zero.")
            
    except ValueError:
        print("Try again. Please enter a number value.")
  

print("")
print("Exercise 3")
print("====================")
print("")

menu = [
    "View Books",
    "Check Out Book",
    "Exit"
]
print("   Menu")
print("------------")
for option in menu:
    index = menu.index(option)
    print(f"{index}: {option}")
    
while True:
    option_response = input("Choose an option: ")
    
    try:
        chosen_option = int(option_response.strip())
        
        if chosen_option in range(len(menu)):
            selected_item = menu[chosen_option]
            print(f"You selected: {selected_item}")
            break
        else:
            print("That menu option does not exist.")
    except ValueError:
        print("You must enter a number from the menu list.")
        

print("")
print("Exercise 4")
print("====================")
print("")

while True:
    items_count_response = input("How many items would you like? ")
    try:
        item_count = int(items_count_response.strip())
        if 0 < item_count <= 20:
            print("Order accepted.")
            break
        else:
            print("Quantity must be between 1 and 20")
       
    
    except ValueError:
        print("Please enter a whole number.")


print("")
print("Exercise 5")
print("====================")
print("")

balance = 150.00

while True:
    withdrawl_response = input("Enter withdrawl amount: ")
    try:
        withdrawl_amount = float(withdrawl_response.strip())
        if withdrawl_amount > 0 and withdrawl_amount <= balance:
            balance -= withdrawl_amount
            print("Withdrawl accepted")
            print(f"Balance: {balance:.2f}")
            break
        elif withdrawl_amount > balance:
            print("Insufficient funds.")
        else:
            print("Withdrawl amount must be greater than zero")
            
    except ValueError:
        print("Please enter a valid amount.")