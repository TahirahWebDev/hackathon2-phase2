"""
Task model and in-memory storage for the Todo CLI application.
"""

class Task:
    """
    Represents a single todo task with ID, description, and completion status.
    """
    def __init__(self, id: int, description: str, completed: bool = False):
        """
        Initialize a new Task instance.
        
        Args:
            id (int): Unique identifier for the task
            description (str): Description of the task
            completed (bool): Completion status, defaults to False
        """
        if not description or not description.strip():
            raise ValueError("Task description cannot be empty")
        
        self.id = id
        self.description = description.strip()
        self.completed = completed
    
    def __repr__(self):
        status = "Complete" if self.completed else "Incomplete"
        return f"Task(id={self.id}, description='{self.description}', status={status})"
    
    def to_dict(self):
        """Convert task to dictionary representation."""
        return {
            "id": self.id,
            "description": self.description,
            "completed": self.completed
        }


class TaskStorage:
    """
    In-memory storage for tasks with basic CRUD operations.
    """
    def __init__(self):
        self.tasks = {}  # Dictionary mapping task ID to Task objects
        self.next_id = 1  # Counter for generating unique task IDs
    
    def add_task(self, description: str) -> Task:
        """
        Add a new task with the given description.
        
        Args:
            description (str): Description of the new task
            
        Returns:
            Task: The newly created Task object
        """
        if not description or not description.strip():
            raise ValueError("Task description cannot be empty")
        
        task = Task(self.next_id, description)
        self.tasks[self.next_id] = task
        self.next_id += 1
        return task
    
    def get_task(self, task_id: int) -> Task:
        """
        Retrieve a task by its ID.
        
        Args:
            task_id (int): ID of the task to retrieve
            
        Returns:
            Task: The task with the given ID
            
        Raises:
            KeyError: If no task with the given ID exists
        """
        if task_id not in self.tasks:
            raise KeyError(f"Task with ID {task_id} does not exist")
        return self.tasks[task_id]
    
    def get_all_tasks(self) -> list:
        """
        Retrieve all tasks.
        
        Returns:
            list: List of all Task objects
        """
        return list(self.tasks.values())
    
    def update_task(self, task_id: int, description: str = None, completed: bool = None) -> Task:
        """
        Update an existing task's description or completion status.
        
        Args:
            task_id (int): ID of the task to update
            description (str, optional): New description for the task
            completed (bool, optional): New completion status for the task
            
        Returns:
            Task: The updated Task object
            
        Raises:
            KeyError: If no task with the given ID exists
        """
        if task_id not in self.tasks:
            raise KeyError(f"Task with ID {task_id} does not exist")
        
        task = self.tasks[task_id]
        
        if description is not None:
            if not description or not description.strip():
                raise ValueError("Task description cannot be empty")
            task.description = description.strip()
        
        if completed is not None:
            task.completed = completed
        
        return task
    
    def delete_task(self, task_id: int) -> bool:
        """
        Delete a task by its ID.
        
        Args:
            task_id (int): ID of the task to delete
            
        Returns:
            bool: True if the task was deleted, False if it didn't exist
        """
        if task_id not in self.tasks:
            return False
        
        del self.tasks[task_id]
        return True
    
    def task_exists(self, task_id: int) -> bool:
        """
        Check if a task with the given ID exists.
        
        Args:
            task_id (int): ID of the task to check
            
        Returns:
            bool: True if the task exists, False otherwise
        """
        return task_id in self.tasks