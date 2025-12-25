"""
Utility functions for the Todo CLI application.
"""


class TodoError(Exception):
    """
    Base exception class for todo application errors.
    """
    pass


class InvalidTaskIdError(TodoError):
    """
    Exception raised when an invalid task ID is provided.
    """
    def __init__(self, task_id):
        self.task_id = task_id
        super().__init__(f"Invalid task ID: {task_id}")


class EmptyTaskDescriptionError(TodoError):
    """
    Exception raised when an empty task description is provided.
    """
    def __init__(self):
        super().__init__("Task description cannot be empty")


def validate_task_id(task_id: str) -> int:
    """
    Validate and convert a task ID string to an integer.
    
    Args:
        task_id (str): Task ID as a string
        
    Returns:
        int: Validated task ID as integer
        
    Raises:
        InvalidTaskIdError: If the task ID is not a valid integer
    """
    try:
        task_id_int = int(task_id)
        if task_id_int <= 0:
            raise InvalidTaskIdError(task_id)
        return task_id_int
    except ValueError:
        raise InvalidTaskIdError(task_id)


def validate_task_description(description: str) -> str:
    """
    Validate a task description.
    
    Args:
        description (str): Task description to validate
        
    Returns:
        str: Validated and stripped task description
        
    Raises:
        EmptyTaskDescriptionError: If the description is empty or contains only whitespace
    """
    if not description or not description.strip():
        raise EmptyTaskDescriptionError()
    return description.strip()