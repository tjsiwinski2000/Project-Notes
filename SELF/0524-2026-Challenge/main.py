#     0524-2026 Gemini Create a dictionary called inventory where keys are item names (strings) and values are their quantities (integers).
#     Start with: {"Blasters": 5, "Space Rations": 50, "Medkits": 10}
#     Write a function add_item(item, quantity) that adds to an existing item's count or creates a new one if it doesn't exist.
#     Write a function view_inventory() that prints the items in a nice, clean format.

inventory={"Blasters": 5, "Space Rations": 50, "Medkits": 10}

def add_item(item, quantity):
    if item in inventory.keys():
        inventory[item] += quantity
    else:
        inventory[item] = quantity
        
def show_inventory():
    for k,v in inventory.items():
        print(f"{k}:\t{v}")
        
def check_alerts():
    for k in inventory.keys():
        if inventory[k] < 15:
            print(f"🚨 CRITICAL LOW: {k} (Only {inventory[k]} left!")

# Write a function restock_plan() that automatically calculates how many of each low-stock item (less than 15) you need to buy to bring its quantity back up to a safe baseline of 50.
# Output a summary of what needs to be ordered.
def restock_plan():
    report = "==RESTOCK REPORT==\n"
    report += "ITEM\t\tQUANTITY\n"
    for k in inventory.keys():
        if inventory[k] < 15:
            report += f"{k}:\t{50-inventory[k]}\n"
    print(report)
            
    
add_item("Blasters",10)  
add_item("Ice Cream",14)     
show_inventory()  
check_alerts()
restock_plan()

#FEEDBACK FROM GEMINI 3:45pm 0524-2026
# In Python, when checking if a key exists in a dictionary, you don't actually need to call .keys(). Checking the dictionary directly is faster and more Pythonic.
# Python

# # Instead of:
# if item in inventory.keys():

# # Do this:
# if item in inventory:

# 2. Dictionary Unpacking in Loops
# In check_alerts and restock_plan, you used for k in inventory.keys(): and then looked up the value using inventory[k]. You can reuse the unpacking trick for k, v in inventory.items(): that you perfectly executed in show_inventory!

# 3. Level 3 Math Tweak
# Your restock_plan() prints out the current low stock, but the prompt asked to calculate how many you need to buy to reach 50.