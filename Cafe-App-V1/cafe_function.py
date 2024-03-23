# Functions for all menu option to be printed out in the loop

def main_menu():
    print("\n1. Exit App")
    print("2. Product Menu")
    print("3. Orders Menu")
    print("4. Courier Menu\n")

def product_menu():
    print("\n1. Product List")
    print("2. Add Products")
    print("3. Go Back to Main Menu\n")

def orders_menu():
    print ("\n1. Orders Dictionary")
    print ("2. Customer Information")
    print ("3. Update Orders")
    print ("4. Go Back to Main Menu\n" )
    
def courier_menu():
    print("\n1. Couriers List")
    print("2. Add New Courier")
    print("3. Return to Main Menu\n")
    
#-------------------------------------------------------------------------------------------------------

#  Product list for all current cafe products, to be listed and updated in the product menu options

product_list = ["Coffee", "Tea", "Cappuccino", "Latte", "Espresso", "Croissant", "Muffin", "Sandwich", "Smoothie"]

#-------------------------------------------------------------------------------------------------------

### All Functions, Lists and Dictionaries related to orders

# Orders list that will be used to record the customer information and the status list that will be used to update the status of customers orders in the orders list
orders = [] 
order_status_list = ['PREPARING', 'SHIPPED', 'DELIVERED']
    
# Function for the Input    
def menu_option():
    option = input("Enter your choice: ")
    return option

# Funtion for the customer inputs, the orders dictionary that will be used and function to append the info to the orders list
def place_order():
    customer_name = input("Enter customer name: ")
    customer_address = input("Enter customer address: ")
    customer_phone = input("Enter customer phone number: ")

    order = {
        'customer_name': customer_name,
        'customer_address': customer_address,
        'customer_phone': customer_phone,
        'status': 'PREPARING'
    }
    
    orders.append(order)
    print("Order placed successfully!")
    
# Viewing orders funtion for if there are orders or not

def view_orders():
    if not orders:
        print("No orders available.")
    else:
        print("Orders:")
        for order in orders:
            print(order)
            
# Funtions for updates the order status. Will show the orders and give option to select order using the index, will give the status options and the status chosen will update the order.

def update_order_status():
    print("Orders:")
    for i, order in enumerate(orders):
        print(f"{i}. {order['customer_name']} - {order['status']}")

    
    order_index = int(input("Enter the index of the order to update: "))


    print("Order Status Options:")
    for i, status in enumerate(order_status_list):
        print(f"{i}. {status}")

    status_index = int(input("Enter the index of the new order status: "))

    orders[order_index]['status'] = order_status_list[status_index]
    print("Order status updated successfully!")
    
#----------------------------------------------------------------------------------------------------------------

# List of couriers 
            
couriers_list = []

def courier_choice_1():
 print("Couriers List:")
 for courier in couriers_list:   # Print all couriers in the list, if no couriers an empty list will show
    print(courier)
    
def courier_choice_2():
    new_courier_name = input("Enter the name of the new courier: ")
    couriers_list.append(new_courier_name)
              
    print(f"Courier '{new_courier_name}' added successfully.")  # Adding couriers name to the couriers list

#-----------------------------------------------------------------------------------------------------------------

#Products 

def display_cafe_products(product_list): # Funtion to list products in a certain format
 print("\nCafe Products:")
 for product in product_list:
    print("- " + product)
    
def product_choice_2():
    print("Adding New Product.")                                               
    while True: 
     new_product = input("\nEnter a new product (or '0' to stop adding): ") # will add products from user input until 0 is inputted
    
     if new_product == '0':
      break
                           
     product_list.append(new_product)
     print(f"{new_product} has been added to the menu.")
                
    print("\nUpdated Cafe Products:")
    display_cafe_products(product_list)
    
     
                
