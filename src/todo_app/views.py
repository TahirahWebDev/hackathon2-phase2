"""
View functions for the Todo CLI application.
Handles user interface and input/output operations.
"""


def display_menu():
    """
    Display the main menu options to the user.
    """
    print("\n" + "="*40)
    print("Todo App Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Mark Task Complete/Incomplete")
    print("6. Exit")
    print("="*40)


def get_user_choice() -> str:
    """
    Prompt the user for their menu choice.
    
    Returns:
        str: The user's menu choice
    """
    return input("Enter your choice (1-6): ").strip()


def get_task_description() -> str:
    """
    Prompt the user for a task description.
    
    Returns:
        str: The task description entered by the user
    """
    return input("Enter task description: ").strip()


def get_task_id(prompt: str = "Enter task ID: ") -> str:
    """
    Prompt the user for a task ID.
    
    Args:
        prompt (str): The prompt to display to the user
        
    Returns:
        str: The task ID entered by the user
    """
    return input(prompt).strip()


def get_task_status() -> str:
    """
    Prompt the user for a task status.
    
    Returns:
        str: The task status ('complete' or 'incomplete') entered by the user
    """
    return input("Enter status (complete/incomplete): ").strip().lower()


def display_tasks(tasks):
    """
    Display all tasks to the user.
    
    Args:
        tasks: List of task objects to display
    """
    if not tasks:
        print("\nNo tasks in the list.")
        return
    
    print("\nYour Tasks:")
    print("-" * 50)
    for task in tasks:
        status = "✓" if task.completed else "○"
        print(f"{status} [{task.id}] {task.description}")
    print("-" * 50)


def display_message(message: str):
    """
    Display a message to the user.
    
    Args:
        message (str): The message to display
    """
    print(f"\n{message}")


def display_error(error_message: str):
    """
    Display an error message to the user.
    
    Args:
        error_message (str): The error message to display
    """
    print(f"\nError: {error_message}")


def display_add_success(task_id: int, description: str):
    """
    Display success message after adding a task.
    
    Args:
        task_id (int): ID of the added task
        description (str): Description of the added task
    """
    print(f"\nTask added successfully!")
    print(f"ID: {task_id}, Description: {description}")


def display_update_success(task_id: int, description: str):
    """
    Display success message after updating a task.
    
    Args:
        task_id (int): ID of the updated task
        description (str): New description of the task
    """
    print(f"\nTask updated successfully!")
    print(f"ID: {task_id}, New Description: {description}")


def display_delete_success(task_id: int):
    """
    Display success message after deleting a task.
    
    Args:
        task_id (int): ID of the deleted task
    """
    print(f"\nTask with ID {task_id} deleted successfully!")


def display_status_change_success(task_id: int, status: str):
    """
    Display success message after changing task status.
    
    Args:
        task_id (int): ID of the task whose status was changed
        status (str): New status of the task
    """
    print(f"\nTask with ID {task_id} marked as {status}!")