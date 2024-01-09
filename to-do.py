""" Stating that this is a To-do list in Python """
# importing sys module for program exit
# standard Python module 
import sys

# initialize empty list for to do list
to_do_list = []

# initialize empty list for marked tasks
marked_tasks_list = []

# function to add a task
def add_task():
    task_choice = input("1) 'Add Task' chosen.\nType new task here:  ").casefold()              
    # use append to add "task_choice" in to_do_list
    to_do_list.append(task_choice)                                                              
    print("Successfully task added.\nTo do list updated:", to_do_list)

# function to remove a task
def remove_task():
    print("2) 'Remove task' chosen. This is your current list:", to_do_list)
    erease_input = input("Type the task to remove here:  ").casefold()                                     

    # check if user input available in to_do_list
    if erease_input in to_do_list:                                                              
        to_do_list.remove(erease_input)                                                        
        print(f'{erease_input} successfully removed. To do list updated:', to_do_list)

    else:                                                                                     
        print(f'{erease_input} not found. Choose tasks available in the to do list.')

# function to View 2 different lists
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

        print(f'{mark_text} is completed. Moved to marked tasks list.')
        print(f'This is the finished tasks list.\n', marked_tasks_list)

    else: print(f'{mark_text} not found in list. Try a text within the list')


# function to exit the program
def exit_program():
    print("Exiting program")
    sys.exit()


# Start while loop
while True:
    # display menu
    display_menu= "\nTo-do list menu:\n1) Add a task\n2) Remove a task\n3) view list\n4) Mark a task\n5) Exit program\n"
    print(display_menu)

    # Prompt user input
    task_choice = input("Choose the number of task:   ")


    try:
        # converts input into integers, catches non-numeric input.
        task_choice = int(task_choice)

        if task_choice == 1:
            add_task()

            # Ask prompt if user wants to return to main menu
            return_menu = input("***Press 'any key' to return to main menu. Press 'n' to exit***:  \n").lower()
            if return_menu == 'any key':
                print("Go back to main menu")
                continue
            elif return_menu == 'n':
                print("Program stops. Goodbye!")
                break

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

        else:
            print("Wrong input. Please enter a number from 1-5\n")

    except ValueError:
        # Tells user to try again if ValueError is caught
        print("Value Error. Please enter a number from 1-5\n")
