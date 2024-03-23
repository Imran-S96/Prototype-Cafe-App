from cafe_function import *

print("*** WELCOME TO THE SHAKE CAFE***")
            


while True:  # While Loop for my menu options, having a main loop and then sub loops. while loop to repeat a block of code until a certain condition is met
    main_menu() 
    choice = menu_option()  # Giving the menu_option() a value as it will be used constantly and will be give diffrernt values to aviod any loop issues
    
    
    if choice == '1':
        print("Exiting the app.")
        break  # Will break the code, stopping the app
    
    
    
    
    elif choice == '2':
        while True:
            product_menu()
            product_choice = menu_option()

            if product_choice == '1':
                display_cafe_products(product_list) # code is executed will go back to product menu

                             
            elif product_choice == '2':
                product_choice_2()
                
                
            elif product_choice == '3':
                print("Going back to Main Menu.")
                break # Break current loop and take us to main menu
            
            
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")
                
                
                
                
            
    
    elif choice == '3':
        while True:
            orders_menu()
            orders_choice = menu_option()
            
        
            if orders_choice == '1':
                print("Orders Dictionary")
                view_orders()  
              
            elif orders_choice == '2':
                place_order()
                
            elif orders_choice == '3':
                update_order_status()
            
            elif orders_choice == '4':
                print("Going back to Main Menu.")
                break # Will break the orders menu loop
            
            else:
                print("Invalid choice. Please enter 1, 2, 3 or 4.")
                
                
                
                
                
    
    elif choice == '4':
        while True:
            courier_menu()
            courier_choice = menu_option()
            
            if courier_choice == '1':
             courier_choice_1()
            
            elif courier_choice == '2':
              courier_choice_2()
            
            elif courier_choice == '3':
                print("Going back to Main Menu.")
                break  # Will break the couriers menu loop
            
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")
                
        
        
        
        
        
    else:
     print("Invalid choice. Please enter 1, 2 , 3 or 4.")
     