"""
Controller functions for the Todo CLI application.
Handles business logic for task operations.
"""
from .models import TaskStorage
from .utils import validate_task_description, validate_task_id, InvalidTaskIdError, EmptyTaskDescriptionError


class TodoController:
    """
    Controller class that handles all business logic for the todo application.
    """
    def __init__(self):
        self.storage = TaskStorage()
    
    def add_task(self, description: str) -> Task:
        """
        Add a new task with the given description.
        
        Args:
            description (str): Description of the new task
            
        Returns:
            Task: The newly created Task object
            
        Raises:
            EmptyTaskDescriptionError: If the description is empty
        """
        validated_description = validate_task_description(description)
        return self.storage.add_task(validated_description)
    
    def get_all_tasks(self) -> list:
        """
        Retrieve all tasks.
        
        Returns:
            list: List of all Task objects
        """
        return self.storage.get_all_tasks()
    
    def update_task(self, task_id_str: str, new_description: str) -> Task:
        """
        Update an existing task's description.
        
        Args:
            task_id_str (str): ID of the task to update as a string
            new_description (str): New description for the task
            
        Returns:
            Task: The updated Task object
            
        Raises:
            InvalidTaskIdError: If the task ID is invalid
            EmptyTaskDescriptionError: If the new description is empty
        """
        task_id = validate_task_id(task_id_str)
        validated_description = validate_task_description(new_description)
        return self.storage.update_task(task_id, description=validated_description)
    
    def delete_task(self, task_id_str: str) -> bool:
        """
        Delete a task by its ID.
        
        Args:
            task_id_str (str): ID of the task to delete as a string
            
        Returns:
            bool: True if the task was deleted, False if it didn't exist
            
        Raises:
            InvalidTaskIdError: If the task ID is invalid
        """
        task_id = validate_task_id(task_id_str)
        return self.storage.delete_task(task_id)
    
    def mark_task_status(self, task_id_str: str, status: str) -> Task:
        """
        Mark a task as complete or incomplete.
        
        Args:
            task_id_str (str): ID of the task to update as a string
            status (str): New status ('complete' or 'incomplete')
            
        Returns:
            Task: The updated Task object
            
        Raises:
            InvalidTaskIdError: If the task ID is invalid
        """
        task_id = validate_task_id(task_id_str)
        
        # Validate status
        if status.lower() not in ['complete', 'incomplete']:
            raise ValueError(f"Invalid status: {status}. Use 'complete' or 'incomplete'.")
        
        completed = (status.lower() == 'complete')
        return self.storage.update_task(task_id, completed=completed)
    
    def task_exists(self, task_id_str: str) -> bool:
        """
        Check if a task with the given ID exists.
        
        Args:
            task_id_str (str): ID of the task to check as a string
            
        Returns:
            bool: True if the task exists, False otherwise
            
        Raises:
            InvalidTaskIdError: If the task ID is invalid
        """
        task_id = validate_task_id(task_id_str)
        return self.storage.task_exists(task_id)