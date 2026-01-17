# Menu Setup
menu = {
    "Tauer Burger": {"price_USD": 8.20, "stock": 9},
    "Small French Fries": {"price_USD": 3.20, "stock": 11},
    "Chicken Wings": {"price_USD": 5, "stock": 8}
}

# Client Balance
import random


client_balance_USD = random.randint(15, 50)

# Available Menu
# First Item
first_item_name = "Tauer Burger"
first_item_price = 8.20
first_item_stock = 9

# Second Item
second_item_name = "Small French Fries"
second_item_price = 3.20
second_item_stock = 11

# Thrid Item
thrid_item_name = "Chicken Wings"
thrid_item_price = 5
thrid_item_stock = 8

# Taking Order / Inputs / Normalization
item_name = input("Enter the name of the item you want to order: ").strip().title()
number_of_item = int(input("Enter the number of items you want to order: ").strip())

# Order Validation
# Validation-1
if not item_name in menu:
    exit("The item you entered is not on the menu!")

# Validation-2
if item_name == first_item_name:
    if not number_of_item <= first_item_stock:
        exit("The amount you entered is not in stock!")

if item_name == second_item_name:
    if not number_of_item <= second_item_stock:
        exit("The amount you entered is not in stock!")

if item_name == thrid_item_name:
    if not number_of_item <= thrid_item_stock:
        exit("The amount you entered is not in stock!")

# Calculation
DISCOUNT_RATE = 15

if menu[item_name]["price_USD"] * number_of_item >= 20:
    total_price_USD = menu[item_name]["price_USD"] * number_of_item * (1 - DISCOUNT_RATE / 100) # USD
    print(f"Your total amount: {total_price_USD:.2f}")
else:
    total_price_USD = menu[item_name]["price_USD"] * number_of_item # USD
    print(f"Your total amount: {total_price_USD:.2f}")

# Payment Confirmation
payment_confirmation = input("Enter Yes to confirm the payment, or No if you do not confirm: ").strip().title() # Yes / No

if payment_confirmation == "No":
    exit("Your order has been canceled!")

# Checkout
customer_names = ["Maria", "Mark", "John", "Jeck"]

import random

if item_name == first_item_name:
    new_stock_amount = first_item_stock - number_of_item
elif item_name == second_item_name:
    new_stock_amount = second_item_stock - number_of_item
elif item_name == thrid_item_name:
    new_stock_amount = thrid_item_stock - number_of_item


if payment_confirmation == "Yes" and client_balance_USD >= total_price_USD:
    new_balance_USD = client_balance_USD - total_price_USD
    print(f"""Dear {random.choice(customer_names)}
Payment successful. Enjoy your meal!
the total price of your item: {total_price_USD:.2f}
Your new balance: {new_balance_USD:.2f}
New stock amount of the item: {new_stock_amount}""")
elif payment_confirmation == "Yes" and client_balance_USD < total_price_USD:
    print("Not enough balance!")

