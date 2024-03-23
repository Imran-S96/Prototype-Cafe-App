from all_cafe_functions import *
import mysql.connector


WelcomeMessage()
        
while True:                                                     # While Loop for my menu options, having a main loop and then sub loops. while loop to repeat a block of code until a certain condition is met
    main_menu() 
    choice = menu_option()                                      # Giving the menu_option() a value as it will be used constantly and will be give diffrernt values to aviod any loop issues
    
    
    if choice == '1':
        ExitMessage()
        break                                                   # Will break the code, stopping the app
    
    
    
    
    elif choice == '2':
        while True:
            product_menu()
            product_choice = menu_option()

            if product_choice == '1':
                MySQLProducts()

                             
            elif product_choice == '2':
                MySQLAddProducts()
                            
            elif product_choice == '3':
                MySQLProducts()
                MySQLDeleteProduct()
                
            elif product_choice == '4':
                MySQLProducts()
                MySQLUpdateProducts()
                                
            elif product_choice == '5':
                print("Going back to Main Menu.")
                break                                           # Break current loop and take us to main menu
            
            
            else:
                print("Invalid choice. Please enter 1, 2, 3, 4 or 5.") # Error checking, if correct input isn't give will print error message
                
                
                
                
            
    
    elif choice == '3':
        while True:
            orders_menu()
            orders_choice = menu_option()
                    
        
            if orders_choice == '1':
                MySQLOrders()
              
            elif orders_choice == '2':
                MySQLAddOrders()
                
            elif orders_choice == '3':
                MySQLOrders()
                MySQLUpdateOrdersStatus()
                
            elif orders_choice == '4':
                MySQLUpdateOrders()
                
            elif orders_choice == '5':
                MySQLOrders()
                MySQLDeleteOrders()
                
            
            elif orders_choice == '6':
                print("Going back to Main Menu.")
                break                                               # Will break the orders menu loop
            
            else:
                print("Invalid choice. Please enter 1, 2, 3, 4, 5 or 6.")   #Error checking, if correct input isn't give will print error message
                
                
                
                
                
    
    elif choice == '4':
        while True:
            courier_menu()
            courier_choice = menu_option()
            
            if courier_choice == '1':
             MySQLCouriers()
            
            elif courier_choice == '2':
              MySQLAddCouriers()
                            
            elif courier_choice == '3':
              MySQLCouriers()
              MySQLDeleteCourier()
              
            elif courier_choice == '4':
              MySQLCouriers()
              MySQLUpdateCouriers()
            
            elif courier_choice == '5':
                print("Going back to Main Menu.")
                break                                           # Will break the couriers menu loop
            
            else:
                print("Invalid choice. Please enter 1, 2, 3, 4 or 5.")  #Error checking, if correct input isn't give will print error message
                
        
        
        
        
        
    else:
     print("Invalid choice. Please enter 1, 2 , 3 or 4.")  #Error checking, if correct input isn't give will print error message
     