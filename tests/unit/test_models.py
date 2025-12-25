"""
Unit tests for the models module of the Todo CLI application.
"""
import pytest
from src.todo_app.models import Task, TaskStorage


class TestTask:
    """Tests for the Task class."""
    
    def test_task_creation(self):
        """Test creating a new task with valid parameters."""
        task = Task(1, "Test task description")
        assert task.id == 1
        assert task.description == "Test task description"
        assert task.completed is False
    
    def test_task_creation_with_completed_status(self):
        """Test creating a new task with completed status."""
        task = Task(1, "Test task description", completed=True)
        assert task.id == 1
        assert task.description == "Test task description"
        assert task.completed is True
    
    def test_task_creation_empty_description(self):
        """Test that creating a task with empty description raises ValueError."""
        with pytest.raises(ValueError):
            Task(1, "")
    
    def test_task_creation_whitespace_description(self):
        """Test that creating a task with whitespace-only description raises ValueError."""
        with pytest.raises(ValueError):
            Task(1, "   ")
    
    def test_task_repr(self):
        """Test the string representation of a task."""
        task = Task(1, "Test task description")
        expected = "Task(id=1, description='Test task description', status=Incomplete)"
        assert repr(task) == expected
        
        task.completed = True
        expected = "Task(id=1, description='Test task description', status=Complete)"
        assert repr(task) == expected
    
    def test_task_to_dict(self):
        """Test converting a task to dictionary representation."""
        task = Task(1, "Test task description", completed=True)
        expected_dict = {
            "id": 1,
            "description": "Test task description",
            "completed": True
        }
        assert task.to_dict() == expected_dict


class TestTaskStorage:
    """Tests for the TaskStorage class."""
    
    def test_initial_state(self):
        """Test that TaskStorage starts with empty tasks and ID counter at 1."""
        storage = TaskStorage()
        assert len(storage.tasks) == 0
        assert storage.next_id == 1
    
    def test_add_task(self):
        """Test adding a task to storage."""
        storage = TaskStorage()
        task = storage.add_task("Test task description")
        
        assert task.id == 1
        assert task.description == "Test task description"
        assert task.completed is False
        assert 1 in storage.tasks
        assert storage.tasks[1] == task
        assert storage.next_id == 2  # Counter should increment
    
    def test_add_task_empty_description(self):
        """Test that adding a task with empty description raises ValueError."""
        storage = TaskStorage()
        with pytest.raises(ValueError):
            storage.add_task("")
    
    def test_get_task(self):
        """Test retrieving an existing task."""
        storage = TaskStorage()
        original_task = storage.add_task("Test task")
        
        retrieved_task = storage.get_task(1)
        assert retrieved_task == original_task
    
    def test_get_nonexistent_task(self):
        """Test that retrieving a non-existent task raises KeyError."""
        storage = TaskStorage()
        with pytest.raises(KeyError):
            storage.get_task(1)
    
    def test_get_all_tasks(self):
        """Test retrieving all tasks."""
        storage = TaskStorage()
        task1 = storage.add_task("First task")
        task2 = storage.add_task("Second task")
        
        all_tasks = storage.get_all_tasks()
        assert len(all_tasks) == 2
        assert task1 in all_tasks
        assert task2 in all_tasks
    
    def test_update_task_description(self):
        """Test updating a task's description."""
        storage = TaskStorage()
        original_task = storage.add_task("Original description")
        
        updated_task = storage.update_task(1, description="Updated description")
        
        assert updated_task.id == 1
        assert updated_task.description == "Updated description"
        assert updated_task.completed is False  # Should remain unchanged
    
    def test_update_task_status(self):
        """Test updating a task's completion status."""
        storage = TaskStorage()
        original_task = storage.add_task("Test task")
        
        updated_task = storage.update_task(1, completed=True)
        
        assert updated_task.id == 1
        assert updated_task.description == "Test task"  # Should remain unchanged
        assert updated_task.completed is True
    
    def test_update_task_both_fields(self):
        """Test updating both description and status."""
        storage = TaskStorage()
        original_task = storage.add_task("Original description")
        
        updated_task = storage.update_task(1, description="New description", completed=True)
        
        assert updated_task.id == 1
        assert updated_task.description == "New description"
        assert updated_task.completed is True
    
    def test_update_nonexistent_task(self):
        """Test that updating a non-existent task raises KeyError."""
        storage = TaskStorage()
        with pytest.raises(KeyError):
            storage.update_task(1, description="New description")
    
    def test_update_task_empty_description(self):
        """Test that updating a task with empty description raises ValueError."""
        storage = TaskStorage()
        storage.add_task("Original description")
        
        with pytest.raises(ValueError):
            storage.update_task(1, description="")
    
    def test_delete_task(self):
        """Test deleting an existing task."""
        storage = TaskStorage()
        storage.add_task("Test task")
        
        result = storage.delete_task(1)
        assert result is True
        assert 1 not in storage.tasks
        assert len(storage.tasks) == 0
    
    def test_delete_nonexistent_task(self):
        """Test deleting a non-existent task."""
        storage = TaskStorage()
        
        result = storage.delete_task(1)
        assert result is False  # Should return False, not raise exception
    
    def test_task_exists(self):
        """Test checking if a task exists."""
        storage = TaskStorage()
        storage.add_task("Test task")
        
        assert storage.task_exists(1) is True
        assert storage.task_exists(2) is False