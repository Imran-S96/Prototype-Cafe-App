import mysql.connector

# Welcome and Exiting Functions

def WelcomeMessage():                                                                    # Function for prininting the Welcome Message
 print("\n","*** WELCOME TO THE SHAKE CAFE ***")
 
def ExitMessage():                                                                       # Function for for printing Exiting App Message
 print("\n","Exiting the app.")



# All Menu Funtions-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def main_menu():                                                                         # Function that prints main menu options
    print("\n1. Exit App")
    print("2. Product Menu")
    print("3. Orders Menu")
    print("4. Courier Menu\n")

def product_menu():                                                                      # Function that prints product menu options
    print("\n1. Products List")
    print("2. Add Products")
    print("3. Delete Products")
    print("4. Update Products")
    print("5. Go Back to Main Menu\n")

def orders_menu():                                                                       # Function that prints orders menu options
    print ("\n1. Orders List")
    print ("2. Add Order")
    print ("3. Update Orders Status")
    print ("4. Update Orders")
    print ("5. Delete Orders")
    print ("6. Go Back to Main Menu\n" )
    
def courier_menu():                                                                      # Function that prints couriers menu options
    print("\n1. Couriers List")
    print("2. Add New Courier")
    print("3. Delete Courier")
    print("4. Update Courier")
    print("5. Return to Main Menu\n")
    
def menu_option():                                                                       # Function used in inputs for all menu options
    option = input("Enter your choice: ")
    return option

# Error Checking Functions----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def get_integer_input(prompt):                                                           # Function thats used to error check for only integer inputs
    while True:                                                                          # Converts user input into an integer, if successful returns user input, if unsuccessful will print the error message
        user_input = input(prompt)
        try:
            integer_value = int(user_input)
            return integer_value
        except ValueError:
            print("Error Invalid Input - Please Enter a Valid Number.")

          
def get_string_input(prompt):                                                            # Function thats used to error check for only string inputs
    while True:                                                                          # Converts user input into a string, if successful returns user input, if unsuccessful will print the error message
        user_input = input(prompt)                                                       
        try:                                                                
            string_value = str(user_input)
            return string_value
        except ValueError:
            print("rror Invalid Input - Please Enter a Valid Input.")
            
def get_float_input(prompt):                                                             # Function thats used to error check for only float inputs
    while True:                                                                          # Converts user input into a float, if successful returns user input, if unsuccessful will print the error message
        user_input = input(prompt)
        try:
            string_value = float(user_input)
            return string_value
        except ValueError:
            print("Error Invalid Input - Please Enter a Valid Number.")
            

# Products----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def MySQLProducts():                                                                     # Function for viewing all Products from the Database
 try:                                                                                    # Opens connection to the MySQL Database
    connection = mysql.connector.connect(host='localhost',
                                         database='Cafe_App',
                                         user='root',
                                         password='password')

    sql_select_Query = "select * from Products"                                          # Selecting everything from the products table 
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    
    records = cursor.fetchall()
    print("\n","Number of Products: ", cursor.rowcount, "\n")                            # Printing the number of products currently in the database

    for row in records:
        print("Id = ", row[0], )                                                         # for loop Printing the entire table row by row ntil no more products left 
        print("Name = ", row[1])
        print("Price  = ", row[2],"\n")

 except mysql.connector.Error as e:                                                      # If any error reading the Database, will print error message
    print("Error reading data")
 finally:                                                                                # Closes connection to the MySql Database
    if connection.is_connected():
        connection.close()
        cursor.close()
        


def MySQLAddProducts():                                                                  # Function for adding products to the Database
 try:                                                                                    # Opens connection to the MySQL Database
    connection = mysql.connector.connect(host='localhost',
                                         database='Cafe_App',
                                         user='root',
                                         password='password')
                                                                                         
    mySql_insert_query = """INSERT INTO Products (Product_name, Price)                   
                           VALUES (%s, %s) """                                           # Shows the table to insert to and the column names to be inserted into
    
    x = get_string_input("Enter New Product Name: ")                                     # Input for the new product name and price
    y = get_float_input("Enter Price: ")

    records_to_insert = [(x,y)]                                                          

    cursor = connection.cursor()
    cursor.executemany(mySql_insert_query, records_to_insert)                            # Where and what inputs are to be inserted 
    connection.commit()                                                                  # Commits the changes to the database
    print("\n",x, "Added to Products")

 except mysql.connector.Error as error:                                                  # If error adding to the Database, will print error message
    print("Failed to Add record")

 finally:                                                                                # Closes connection to the MySql Database
    if connection.is_connected():
        cursor.close()
        connection.close()
        


def MySQLDeleteProduct():                                                                # Function for deleting products from the Database
 try:                                                                                    # Opens connection to the MySQL Database
    connection = mysql.connector.connect(host='localhost',
                                         database='Cafe_App',
                                         user='root',
                                         password='password')

    mySql_delete_query = "DELETE FROM Products WHERE Product_id = %s"                    # Selecting the table and id from where the record should be deleted 
    
    
    x = get_integer_input("Enter Product id to Delete : ")                               # Getting the users input for the Product id
   

    records_to_insert = (x,)

    cursor = connection.cursor()
    cursor.execute(mySql_delete_query, records_to_insert)                                # Where and what inputs are to be deleted
    connection.commit()                                                                  # Commits the changes to the database
    print("Product Deleted")

 except mysql.connector.Error as error:                                                  # If error deleting from the Database, will print error message
    print("Failed to Delete record")

 finally:                                                                                # Closes connection to the MySql Database
    if connection.is_connected():
        cursor.close()
        connection.close()
        



def MySQLUpdateProducts():                                                               # Function for updating products in the Database                                      
 try:                                                                                    # Opens connection to the MySQL Database
    connection = mysql.connector.connect(host='localhost', 
                                         database='Cafe_App',
                                         user='root',
                                         password='password')
    
    table_name = "Products"                                                              # All variables that will be used in gettinng user input
    primary_key_column = "Product_id"       
    update_columns = {"Product_name": "", "Price": ""} 
    
    primary_key_value = get_integer_input(f"Enter the {primary_key_column} of the Product to update: ")                    # Getting user input for product id to update

    update_query = f"UPDATE {table_name} SET "                                                                             # Where the couriers will be updated from
    update_query += ", ".join([f"{column} = %s" for column in update_columns.keys()])
    update_query += f" WHERE {primary_key_column} = %s"

    a = get_string_input("Enter New Product: ")                                                                            # User input for updated product and price
    b = get_float_input("Enter New Price: ")
    update_values = [a, b]

   
    cursor = connection.cursor()
    cursor.execute(update_query, update_values + [primary_key_value])                                                      # Update the values with the users input 
    connection.commit()                                                                                                    # Will commit the changes
    print("Product Updated")
    
 except mysql.connector.Error as error:                                                                                    # If error updating the Database, will print error message
    print("Failed to Update record")

 finally:                                                                                                                  # Closes connection to the MySql Database      
    if connection.is_connected():
        cursor.close()
        connection.close()
        
    
    
# Couriers Function ------------------------------------------------------------------------------------------------------------------------------------------------------------------------   

def MySQLCouriers():                                                                                                       # Function for viewing all Couriers from the Database
 try:                                                                                                                      # Opens connection to the MySQL Database
    connection = mysql.connector.connect(host='localhost',
                                         database='Cafe_App',
                                         user='root',
                                         password='password')

    sql_select_Query = "select * from Couriers"                                                                            # Selecting everything from the Couriers table 
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    print("Total number of Couriers: ", cursor.rowcount, "\n")                                                             # Printing the number of couriers currently in the database

    for row in records:                                                                                                    # for loop Printing the entire table row by row ntil no more couriers left 
        print("Id = ", row[0], )
        print("Name = ", row[1])
        print("Number  = ", row[2],"\n")

 except mysql.connector.Error as e:                                                                                        # If any error reading the Database, will print error message
    print("Error reading data")
 finally:                                                                                                                  # Closes connection to the MySql Database
    if connection.is_connected():
        connection.close()
        cursor.close()
        
        

        

def MySQLAddCouriers():                                                                                                    #  Function for adding Couriers to the Database
 try:                                                                                                                      # Opens connection to the MySQL Database
    connection = mysql.connector.connect(host='localhost',
                                         database='Cafe_App',
                                         user='root',
                                         password='password')
                                                                             
    mySql_insert_query = """INSERT INTO Couriers (Couriers_name, Couriers_number) 
                           VALUES (%s, %s) """                                                                             # Shows the table to insert to and the column names to be inserted into
    
    x = get_string_input("Enter New Courier: ")                                                                            # Input for the new Courier name and number
    y = get_integer_input("Enter Couriers Number: ")

    records_to_insert = [(x,y)]

    cursor = connection.cursor()
    cursor.executemany(mySql_insert_query, records_to_insert)                                                              # Where and what inputs are to be inserted 
    connection.commit()                                                                                                    # Commits the changes to the database
    print(x, "Added to Couriers")

 except mysql.connector.Error as error:                                                                                    # If error adding to the Database, will print error message
    print("Failed to Add record")

 finally:                                                                                                                  # Closes connection to the MySql Database
    if connection.is_connected():
        cursor.close()
        connection.close()
        
        


        
        
        
def MySQLDeleteCourier():                                                                                                  # Function for deleting Couriers from the Database
 try:                                                                                                                      # Opens connection to the MySQL Database
    connection = mysql.connector.connect(host='localhost',
                                         database='Cafe_App',
                                         user='root',
                                         password='password')

    mySql_delete_query = "DELETE FROM Couriers WHERE Couriers_id = %s"                                                     # Selecting the table and id from where the record should be deleted 
    
    
    x = get_integer_input("Enter Courier id to Delete : ")                                                                 # Getting the users input for the Courier id
   

    records_to_insert = (x,)

    cursor = connection.cursor()
    cursor.execute(mySql_delete_query, records_to_insert)                                                                  # Where and what inputs are to be deleted
    connection.commit() # Commits the changes to the database
    print("Courier Deleted")

 except mysql.connector.Error as error:                                                                                    # If error deleting from the Database, will print error message
    print("Failed to Delete record")

 finally:                                                                                                                  # Closes connection to the MySql Database
    if connection.is_connected():
        cursor.close()
        connection.close()
        
        
        


        

def MySQLUpdateCouriers():                                                                                                 # Function for updating Couriers in the Database  
 try:                                                                                                                      # Opens connection to the MySQL Database
    connection = mysql.connector.connect(host='localhost',
                                         database='Cafe_App',
                                         user='root',
                                         password='password')
    
    table_name = "Couriers"                                                                                                # All variables that will be used in gettinng user input
    primary_key_column = "Couriers_id"
    update_columns = {"Couriers_name": "", "Couriers_number": ""}
    
    primary_key_value = get_integer_input(f"Enter the {primary_key_column} of the Courier to update: ")                    # Getting user input for Couriers id to update

    update_query = f"UPDATE {table_name} SET "                                                                             # Where the couriers will be updated from
    update_query += ", ".join([f"{column} = %s" for column in update_columns.keys()])
    update_query += f" WHERE {primary_key_column} = %s"

    a = get_string_input("Enter New Couriers_name: ")                                                                      # User input for updated Courier name and number
    b = get_integer_input("Enter New Couriers_number: ")

    update_values = [a, b]

   
    cursor = connection.cursor()
    cursor.execute(update_query, update_values + [primary_key_value])                                                      # Update the values with the users input 
    connection.commit()                                                                                                    # Will commit the changes
    print("Courier Updated")
    
 except mysql.connector.Error as error:                                                                                    # If error updating the Database, will print error message
    print("Failed to Update record")

 finally:                                                                                                                  # Closes connection to the MySql Database 
    if connection.is_connected():
        cursor.close()
        connection.close()
        

        
# Orders Functions-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


def MySQLOrders():                                                                                                         # Function for viewing all Orders from the Database
 try:                                                                                                                      # Opens connection to the MySQL Database
    connection = mysql.connector.connect(host='localhost',
                                         database='Cafe_App',
                                         user='root',
                                         password='password')

    sql_select_Query = "select * from Orders"                                                                              # Selecting everything from the orders table 
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    
    records = cursor.fetchall()
    print("Total number of Orders: ", cursor.rowcount, "\n")                                                               # Printing the number of orders currently in the database

    for row in records:                                                                                                    # for loop Printing the entire table row by row until no more orders left
        print("Order_id = ", row[0], )
        print("Customer_name = ", row[1])
        print("Customer_address  = ", row[2])
        print("Customer_phone  = ", row[3])
        print("Couriers_id  = ", row[4],)
        print("Order_status_id  = ", row[5],)
        print("Product_id  = ", row[6],"\n")

 except mysql.connector.Error as e:                                                                                        # If any error reading the Database, will print error message
    print("Error reading data")
 finally:                                                                                                                  # Closes connection to the MySql Database
    if connection.is_connected():
        connection.close()
        cursor.close()
        
        
        
        
        
def MySQLDeleteOrders():                                                                                                   # Function for deleting orders from the Database
 try:                                                                                                                      # Opens connection to the MySQL Database
    connection = mysql.connector.connect(host='localhost',
                                         database='Cafe_App',
                                         user='root',
                                         password='password')

    mySql_delete_query = "DELETE FROM Orders WHERE Order_id = %s"                                                          # Selecting the table and id from where the record should be deleted
    
    
    x = get_integer_input("Enter Order_id to Delete : ")                                                                   # Getting the users input for the order id
   

    records_to_insert = (x,)

    cursor = connection.cursor()
    cursor.execute(mySql_delete_query, records_to_insert)                                                                  # Where and what inputs are to be deleted
    connection.commit()                                                                                                    # Commits the changes to the database
    print("Order Deleted")

 except mysql.connector.Error as error:                                                                                    # If error deleting from the Database, will print error message
    print("Failed to Delete record")

 finally:                                                                                                                  # Closes connection to the MySql Database
    if connection.is_connected():
        cursor.close()
        connection.close()
        



def MySQLAddOrders():                                                                                                      # Function for adding products to the Database
    try:                                                                                                                   # Opens connection to the MySQL Database
        connection = mysql.connector.connect(host='localhost',
                                             database='Cafe_App',
                                             user='root',
                                             password='password')

        mySql_insert_query = """INSERT INTO Orders (Customer_name, Customer_address, Customer_phone, Couriers_id, Order_status_id, Product_id) 
                               VALUES (%s, %s, %s, %s, %s, %s) """                                                                                       # Shows the table to insert to and the column names to be inserted int
        
        x = get_string_input("Enter Customer_name: ")                                                                                                    # All Input add customer, courier and order information
        y = get_string_input("Enter Customer_address: ")
        z = get_integer_input("Enter Customer_phone: ")
        MySQLCouriers()
        a = get_integer_input("Enter Couriers_id: ")
        MySQLOrders_Status()
        b = get_integer_input("Enter Order_status_id: ")
        MySQLProducts()
        

        products = []
        while True:                                                                                                                                      # A loop to add in multiple product id's, each new product will creat a new order with the same customer and courier info
            product_id = get_integer_input("Enter Product_id (enter 0 to stop): ")
            if product_id == 0:
                break
            products.append(product_id)

        records_to_insert = [(x, y, z, a, b, product_id) for product_id in products]

        cursor = connection.cursor()
        cursor.executemany(mySql_insert_query, records_to_insert)                                                                                        # Where and what inputs are to be inserted 
        connection.commit()                                                                                                                              # Commits the changes to the database
        print("\n","Order Placed Successfully")

    except mysql.connector.Error as error:                                                                                                               # If error adding to the Database, will print error message
        print("Failed to Add record")

    finally:                                                                                                                                             # Closes connection to the MySql Database
        if connection.is_connected():
            cursor.close()
            connection.close()
        
        
        
        
        
def MySQLUpdateOrdersStatus():                                                                                                                           # Function for updating order status in the Database 
 try:                                                                                                                                                    # Opens connection to the MySQL Database
    connection = mysql.connector.connect(host='localhost',
                                         database='Cafe_App',
                                         user='root',
                                         password='password')
    
    table_name = "Orders"                                                                                                                                # All variables that will be used in getting user inpput
    primary_key_column = "Order_id"
    update_columns = {"Order_status_id": ""}
    
    primary_key_value = get_integer_input(f"Enter the {primary_key_column} of the Order Status to update: ")                                             # Getting user input for order status id to update

    update_query = f"UPDATE {table_name} SET "
    update_query += ", ".join([f"{column} = %s" for column in update_columns.keys()])
    update_query += f" WHERE {primary_key_column} = %s"

    MySQLOrders_Status()      
    a = get_integer_input ("Enter New Order Status: ")                                                                                                   # User input for updating orders status
    
    update_values = [a]

   
    cursor = connection.cursor()
    cursor.execute(update_query, update_values + [primary_key_value])                                                                                    # Update the values with the users input 
    connection.commit()                                                                                                                                  # Will commit changes
    print("Order Status Updated")
    
 except mysql.connector.Error as error:                                                                                                                  # If error updating the Database, will print error message
    print("Failed to Update record")

 finally:                                                                                                                                                # Closes connection to the MySql Database  
    if connection.is_connected():
        cursor.close()
        connection.close()
        



        
def MySQLUpdateOrders():                                                                                                                                 # Function for updating orders in the Database
 try:                                                                                                                                                    # Opens connection to the MySQL Database
    connection = mysql.connector.connect(host='localhost',
                                         database='Cafe_App',
                                         user='root',
                                         password='password')
    
    table_name = "Orders"                                                                                                                                # All variables that will be used in getting user input
    primary_key_column = "Order_id"
    update_columns = {"Customer_name": "", "Customer_address": "", "Customer_phone": "", "Product_id": "", "Couriers_id": ""}
    
    MySQLOrders()
    primary_key_value = get_integer_input(f"Enter the {primary_key_column} of the Order to update: ")                                                    # Getting user input for order id to update

    update_query = f"UPDATE {table_name} SET "
    update_query += ", ".join([f"{column} = %s" for column in update_columns.keys()])
    update_query += f" WHERE {primary_key_column} = %s"

    a = get_string_input("Enter New Customer Name: ")                                                                                                    # All User input for updating all orders info
    b = get_string_input("Enter New Customer Address: ")
    c = get_integer_input("Enter New Customer Phone: ")
    MySQLProducts()
    d = get_integer_input("Enter New Product ID: ")
    MySQLCouriers()
    e = get_integer_input("Enter New Couriers ID: ")

    update_values = [a, b, c, d, e]

   
    cursor = connection.cursor()
    cursor.execute(update_query, update_values + [primary_key_value])                                                                                    # Update the values with the users input 
    connection.commit()                                                                                                                                  # Will commit the changes
    print("Order Updated")
    
 except mysql.connector.Error as error:                                                                                                                  # If error updating the Database, will print error message
    print("Failed to Update record")

 finally:                                                                                                                                                # Closes connection to the MySql Database  
    if connection.is_connected():
        cursor.close()
        connection.close()





def MySQLOrders_Status():                                                                                                                                # Function for viewing all order status from the Database
 try:                                                                                                                                                    # Opens connection to the MySQL Database
    connection = mysql.connector.connect(host='localhost',
                                         database='Cafe_App',
                                         user='root',
                                         password='password')

    sql_select_Query = "select * from Order_status"                                                                                                      # Selecting everything from the orders status table 
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    
    records = cursor.fetchall()
    print("Order Status: ", "\n") 

    for row in records:                                                                                                                                  # for loop Printing the entire table row by row until no more order status left
        print("Order_status_id = ", row[0], )
        print("Order_status = ", row[1],"\n")

 except mysql.connector.Error as e:                                                                                                                      # If any error reading the Database, will print error message
    print("Error reading data")
 finally:                                                                                                                                                # Closes connection to the MySql Database
    if connection.is_connected():
        connection.close()
        cursor.close()