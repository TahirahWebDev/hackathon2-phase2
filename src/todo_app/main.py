"""
Main entry point for the Todo CLI application.
Contains the main application loop and menu handling.
"""
from .views import (
    display_menu, get_user_choice, get_task_description, 
    get_task_id, get_task_status, display_tasks, 
    display_message, display_error, display_add_success,
    display_update_success, display_delete_success,
    display_status_change_success
)
from .controllers import TodoController
from .utils import InvalidTaskIdError, EmptyTaskDescriptionError


def main():
    """
    Main application loop for the Todo CLI application.
    """
    controller = TodoController()
    print("Welcome to the Todo CLI Application!")
    
    while True:
        try:
            display_menu()
            choice = get_user_choice()
            
            if choice == '1':
                # Add Task
                description = get_task_description()
                try:
                    task = controller.add_task(description)
                    display_add_success(task.id, task.description)
                except EmptyTaskDescriptionError as e:
                    display_error(str(e))
            
            elif choice == '2':
                # View Tasks
                tasks = controller.get_all_tasks()
                display_tasks(tasks)
            
            elif choice == '3':
                # Update Task
                task_id = get_task_id("Enter task ID to update: ")
                try:
                    if controller.task_exists(task_id):
                        new_description = get_task_description()
                        try:
                            task = controller.update_task(task_id, new_description)
                            display_update_success(task.id, task.description)
                        except EmptyTaskDescriptionError as e:
                            display_error(str(e))
                    else:
                        display_error(f"Task with ID {task_id} does not exist")
                except InvalidTaskIdError as e:
                    display_error(str(e))
            
            elif choice == '4':
                # Delete Task
                task_id = get_task_id("Enter task ID to delete: ")
                try:
                    if controller.task_exists(task_id):
                        success = controller.delete_task(task_id)
                        if success:
                            display_delete_success(task_id)
                    else:
                        display_error(f"Task with ID {task_id} does not exist")
                except InvalidTaskIdError as e:
                    display_error(str(e))
            
            elif choice == '5':
                # Mark Task Complete/Incomplete
                task_id = get_task_id("Enter task ID to mark: ")
                try:
                    if controller.task_exists(task_id):
                        status = get_task_status()
                        try:
                            task = controller.mark_task_status(task_id, status)
                            display_status_change_success(task.id, "complete" if task.completed else "incomplete")
                        except ValueError as e:
                            display_error(str(e))
                    else:
                        display_error(f"Task with ID {task_id} does not exist")
                except InvalidTaskIdError as e:
                    display_error(str(e))
            
            elif choice == '6':
                # Exit
                display_message("Thank you for using the Todo CLI Application!")
                break
            
            else:
                display_error("Invalid choice. Please enter a number between 1 and 6.")
        
        except KeyboardInterrupt:
            display_message("\n\nApplication interrupted. Goodbye!")
            break
        except Exception as e:
            display_error(f"An unexpected error occurred: {str(e)}")


if __name__ == "__main__":
    main()