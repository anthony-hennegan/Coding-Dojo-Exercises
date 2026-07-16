
print("Exercise 1")

user_age = input("How old are you? ")
print("")

try:
    user_age = int(user_age)
    
    user_age_dict = {
        "age" : user_age,
        "data_type" : type(user_age)
    }
    
    print("Age Data")
    print("---------------")
    
    for key, value in user_age_dict.items():
        print(f"{key}: {value}")
    
except ValueError:
    print("Please type a number.")
    print("")




    
print("")
print("====================")
print("Exercise 2")
print("")

item_count = input("How many items would you like? ")
print("")

try:
    item_count = int(item_count)
    if item_count > 0:
        print(f"{item_count} items.")
    elif item_count <= 0:
        print("Quantity must be greater than zero.")

except ValueError:
    print("Please enter a valid whole number.")

print("")
print("====================")
print("Exercise 3")
print("")

user_temp_response = input("What is the temperature in Farenheit? ")
print("")

try:
    fahrenheit = float(user_temp_response)
    celcius = (fahrenheit - 32) * 5 / 9
    print(f"Temperature: {celcius:.2f}C")
except ValueError:
    print("Please enter a whole number or decimal.")


print("")
print("====================")
print("Exercise 4")
print("")

first_number = input("Enter a number: ")
second_number = input("Enter another number: ")

try:
    first_number = int(first_number.strip())
    second_number = int(second_number.strip())
    
    divide_by_first = first_number / second_number
    
    print(f"Result: {divide_by_first}")
    
except ValueError:
    print("Please enter a whole number.")
    
except ZeroDivisionError:
    print("The second number cannot be zero.")

print("")
print("====================")
print("Exercise 5")
print("")

products = [
    "Hammer",
    "Saw",
    "Drill",
]

for product in products:
    index = products.index(product)
    print(f"{index}:{product}")
    
select_product_response = input("Enter a product number: ")
try:
    product_number = int(select_product_response.strip())
    print(products[product_number])
except ValueError:
    print("Please enter a whole number.")
except IndexError:
    print("That product does not exist.")