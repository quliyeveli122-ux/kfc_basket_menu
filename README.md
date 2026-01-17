# """
# Big Task: KFC Menu & Client Simulation

# You are going to build a simple terminal-based KFC ordering system.

# 1. Menu Setup:
#    Create a dictionary called `menu` where each key is the item name, and the value is another dictionary that contains:
#    - "price": price of the item
#    - "stock": how many pieces are available

#    Example:
#    menu = {
#        "Zinger Burger": {"price": 5.5, "stock": 10},
#        "Fries": {"price": 2.0, "stock": 20},
#        "Chicken Wings": {"price": 4.0, "stock": 15},
#        ...
#    }

# 2. Client Balance:
#    Generate a random balance for the client between $15 and $50.
#    Use: `import random` and `balance = random.randint(15, 50)`

# 3. Display Menu:
#    Show the available menu to the client in a readable format:
#    - Item name
#    - Price
#    - Stock available

# 4. Taking Order:
#    Ask the client which item they want and how many units.
#    (You can simulate one order only for now — no need for multiple items.)

# 5. Order Validation:
#    - Check if the item exists in the menu.
#    - Check if the requested amount is available in stock.
#    - Calculate the total price.

# 6. Payment:
#    Show the total bill.
#    Ask the client to confirm the payment by typing `Y` or `Yes`.
#    If the client doesn't confirm, print "Order cancelled".

# 7. Checkout:
#    - If the client confirms and has enough balance:
#        • Subtract the total from their balance.
#        • Subtract the ordered amount from the stock.
#        • Show "Payment successful. Enjoy your meal!"
#        • Show new balance.
#    - If the balance is not enough, show "Not enough balance".

# 8. Final Stock:
#    After the process, print the updated stock for all menu items.

# Bonus ideas:
#    - Add more than one order step.
#    - Apply discount if the total order is more than $20.
#    - Randomly generate a customer name.

# Requirements:
#    ✔ Use dicts for menu and item info  
#    ✔ Use `if` and ternary operator where possible  
#    ✔ No loops required — only one order is enough  
#    ✔ Use `in`, `len`, `sum`, `random.randint` if needed  
# """
