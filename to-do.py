""" Stating that this is a To-do list in Python """
# importing sys module for program exit
# standard Python module 
import sys

# initialize empty list in Python to do list 
to_do_list = []

# initialize empty list for marked tasks or completed tasks
marked_tasks_list = []

# function to add a task
def add_task():
    task_choice = input("1) 'Add Task' chosen.\nType new task here:  ").casefold()              
    # casefold() is used to convert the input to lowercase, ensuring consistency
    # use append to add "task_choice" in to_do_list and a way to add an element to the end of a list.
    to_do_list.append(task_choice) 

    # prints a confirmation message, indicating that the task has been successfully added. 
    # It also displays the updated to-do list by printing the contents of the to_do_list.                                                             
    print("Successfully task added.\nTo do list updated:", to_do_list)

# function to remove a task
def remove_task():
    # prints a message indicating that the user has chosen to remove a task and displays the current to-do list using to_do_list.
    print("2) 'Remove task' chosen. This is your current list:", to_do_list)

    # asks the user to enter the task they want to remove
    erase_input = input("Type the task to remove here:  ").casefold()                                     

    # checks if user input is available in to_do_list
    # If the entered task is found in the to-do list, this line removes it using the remove() method of the list
    # If the task was found and successfully removed, a confirmation message is printed along with the updated to-do list.
    # If the task is not found in the to-do list, an error message is printed, instructing the user to choose tasks that are available in the to-do list.
    if erase_input in to_do_list:                                                              
        to_do_list.remove(erase_input)                                                        
        print(f'{erase_input} successfully removed. To do list updated:', to_do_list)
    else:                                                                                     
        print(f'{erase_input} not found. Choose tasks available in the to do list.')

# function to View 2 different lists
# prints a message indicating that the user has chosen to view the task lists. 
# then displays the current to-do list using to_do_list.
# displays the list of finished tasks
def view_task():
    print(f'3) View task list chosen.\n Current to do list:', to_do_list)
    print(f' This is the finished tasks list:', marked_tasks_list)


# function to mark a completed task.
def mark_complete_task():
    print(f'This is your current list', to_do_list)
    # take input for text to mark
    mark_text = input("Mark this text from the list:  ").casefold()

    # Check if the task to mark exists in the to_do_list
    if mark_text in to_do_list:

        # Transfer mark_text to marked_taskes_list with append function
        marked_tasks_list.append(mark_text)

        # Remove mark_text from to_do_list with remove function
        to_do_list.remove(mark_text)
        # If the entered text is found in the to-do list
        # prints a message indicating that the task is completed. 
        # It also states that the task has been moved to the marked tasks list.
        print(f'{mark_text} is completed. Moved to marked tasks list.')
        # prints the current contents of the marked tasks list (marked_tasks_list), showing the user the updated list of completed tasks.
        print(f'This is the finished tasks list.\n', marked_tasks_list)
        # prints an error message if the entered text is not found in the to do list 
    else: print(f'{mark_text} not found in list. Try a text within the list')


# function to exit the program
# prints a message informing the user that the program is exiting.
# It stops the program's execution immediately.Using the exit() function from the sys module to terminate the program.
def exit_program(): 
    print("Exiting program")
    sys.exit()



# initiates an infinite while loop, creating a menu-driven interface for a to-do list.
# Start while loop
while True:
    # display menu
    # creates a string variable named display_menu containing the menu options for the to-do list program. 
    # Each option is numbered and corresponds to a specific action the user can take.
    # prints the menu, displaying the available options to the user.
    display_menu= "\nTo-do list menu:\n1) Add a task\n2) Remove a task\n3) view list\n4) Mark a task\n5) Exit program\n"
    print(display_menu)

    # prompts the user to enter a number corresponding to their chosen task from the displayed menu. 
    # The entered choice is stored in the variable task_choice.
    task_choice = input("Choose the number of task:   ")

  try: 
    # convert the user's input (which is initially a string) into an integer using the int() function. 
    # This is done because the menu options are represented as numbers, and the program needs to determine which action the user has chosen based on this integer.
        task_choice = int(task_choice)
      
# If the conversion to an integer is successful, check whether the user's choice is equal to 1, 
# which corresponds to the option of adding a task in the menu
# If the user has chosen to add a task (since task_choice is 1), call the add_task() function.
        if task_choice == 1:
            add_task()

            # Ask if user wants to return to main menu
            # displays a message asking the user to either press any key to return to the main menu or enter 'n' to exit.
            # the lower() method is used to convert the input to lowercase for case-insensitive comparison.
            # checks if the user entered 'any key' (which is not an actual key but a representation here). 
            # If true, it prints a message indicating that the program is going back to the main menu, and the continue statement is used to restart the loop, displaying the main menu again.
            # If the user entered 'n', prints a goodbye message and breaks out of the loop, effectively stopping the program.
            return_menu = input("***Press 'any key' to return to main menu. Press 'n' to exit***:  \n").lower()
            if return_menu == 'any key':
                print("Go back to main menu")
                continue
            elif return_menu == 'n':
                print("Program stops. Goodbye!")
                break
            # checks if the user's choice (stored in the variable task_choice) is equal to 2. The elif statement is short for "else if", 
            # and it introduces an additional condition to be checked only if the previous conditions in the if-elif-else structure are not true.
            # If the condition is true (meaning the user chose 2), it calls the remove_task() function.
        elif task_choice == 2:
            remove_task()

            return_menu = input("***Press 'any key' to return to main menu. Press 'n' to exit***:  \n").lower()
            if return_menu == 'any key':
                print("Go back to main menu")
                continue
            elif return_menu == 'n':
                print("Program stops. Goodbye!")
                break

        elif task_choice == 3:
            view_task()

            return_menu = input("***Press 'any key' to return to main menu. Press 'n' to exit***:  \n")
            if return_menu == 'any key':
                print("Go back to main menu")
                continue
            elif return_menu == 'n':
                print("Program stops. Goodbye!")
                break

        elif task_choice == 4:
            mark_complete_task()

            return_menu = input("***Press 'any key' to return to main menu. Press 'n' to exit***:  \n")
            if return_menu == 'any key':
                print("Go back to main menu")
                continue
            elif return_menu == 'n':
                print("Program stops. Goodbye!")
                break

        elif task_choice == 5:
            exit_program()
            
      # If the user's input for the menu choice is not 1, 2, 3, 4, or 5, this block is executed. 
      # It prints an error message, informing the user that the input is incorrect, and prompts them to enter a number from 1 to 5.
        else:
            print("Wrong input. Please enter a number from 1-5\n")

    except ValueError:
        # catches a ValueError exception. 
        # If the user enters a value that cannot be converted to an integer (e.g., a letter or a symbol), a ValueError occurs. 
        print("Value Error. Please enter a number from 1-5\n")
