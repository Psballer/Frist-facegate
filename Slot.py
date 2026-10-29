slot = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
while True:
    print("present parking lot: ")
    print(slot)
    
    full_up = 0
    empty = 0
    for space in slot:
        if space == 0:
            full_up = full_up + 1
        else:
            empty = empty + 1
            
    print("full_up: " + str(full_up))
    print("present slot: " + str(empty))
    
    
    print("1: Park")
    print("2: Choose slot to park")
    print("3: Exit the parking slot")
    print("4: leave the program")
    
    choice = input("Choose any option from (1-4): ")
    if choice == "1":
           available_space = False
           for index in range(20):
                if slot[index] == 0:
                    slot[index] = 1
                    slot_number = index + 1
                    print("You have successfully park" + str(slot_number))
                    available_space = True
                    break 
                
    if choice == "2":
       available_space = False
       for index in range(20):
            if slot[index] == 0:
                slot[index] = 2
                slot_number = index + 1
                print("You have successfully choose a slot to park" + str(slot_number))
                available_space = True
                break
    
    
    
#    new_array[index] = '0
#input = print("Enter your parking slot: ")
#index = input -1
#
#     new_array[index] = 1

#new_array_list =[0] * 20
#print(new_array_list)
#input = print("Enter your parking slot: ")
#for index in new_array_list:
#    if input ==[0]:
#        print('1')

#main_menu = """
#print("Available Parking space", new_list)
#list of praking menu functions
#1: Parking slot
#2: Enter car number
#3: Available space
#4: Enter your name
#5: Exit (yes/no)
#"""
#print(main_menu)
#main_menu_prompt = int(input('Enter a menu function: '))
#match(main_menu_prompt):
#    case 1:
#        user_input(print(input("Enter a menu: ")))
#        print("Parking slot")


