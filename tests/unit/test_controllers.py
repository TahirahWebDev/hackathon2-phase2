"""
Unit tests for the controllers module of the Todo CLI application.
"""
import pytest
from src.todo_app.controllers import TodoController
from src.todo_app.utils import InvalidTaskIdError, EmptyTaskDescriptionError


class TestTodoController:
    """Tests for the TodoController class."""
    
    def setup_method(self):
        """Set up a fresh controller for each test."""
        self.controller = TodoController()
    
    def test_add_task(self):
        """Test adding a new task."""
        task = self.controller.add_task("Test task description")
        
        assert task.id == 1
        assert task.description == "Test task description"
        assert task.completed is False
    
    def test_add_task_empty_description(self):
        """Test that adding a task with empty description raises EmptyTaskDescriptionError."""
        with pytest.raises(EmptyTaskDescriptionError):
            self.controller.add_task("")
    
    def test_add_task_whitespace_description(self):
        """Test that adding a task with whitespace-only description raises EmptyTaskDescriptionError."""
        with pytest.raises(EmptyTaskDescriptionError):
            self.controller.add_task("   ")
    
    def test_get_all_tasks(self):
        """Test retrieving all tasks."""
        task1 = self.controller.add_task("First task")
        task2 = self.controller.add_task("Second task")
        
        all_tasks = self.controller.get_all_tasks()
        
        assert len(all_tasks) == 2
        assert task1 in all_tasks
        assert task2 in all_tasks
    
    def test_update_task(self):
        """Test updating a task's description."""
        original_task = self.controller.add_task("Original description")
        
        updated_task = self.controller.update_task("1", "Updated description")
        
        assert updated_task.id == 1
        assert updated_task.description == "Updated description"
        assert updated_task.completed is False  # Should remain unchanged
    
    def test_update_task_invalid_id(self):
        """Test that updating a task with invalid ID raises InvalidTaskIdError."""
        with pytest.raises(InvalidTaskIdError):
            self.controller.update_task("invalid", "New description")
        
        with pytest.raises(InvalidTaskIdError):
            self.controller.update_task("0", "New description")
        
        with pytest.raises(InvalidTaskIdError):
            self.controller.update_task("-1", "New description")
    
    def test_update_task_nonexistent(self):
        """Test that updating a non-existent task raises KeyError."""
        with pytest.raises(KeyError):
            self.controller.update_task("1", "New description")
    
    def test_update_task_empty_description(self):
        """Test that updating a task with empty description raises EmptyTaskDescriptionError."""
        self.controller.add_task("Original description")
        
        with pytest.raises(EmptyTaskDescriptionError):
            self.controller.update_task("1", "")
    
    def test_delete_task(self):
        """Test deleting an existing task."""
        self.controller.add_task("Test task")
        
        result = self.controller.delete_task("1")
        
        assert result is True
        assert len(self.controller.get_all_tasks()) == 0
    
    def test_delete_task_invalid_id(self):
        """Test that deleting a task with invalid ID raises InvalidTaskIdError."""
        with pytest.raises(InvalidTaskIdError):
            self.controller.delete_task("invalid")
        
        with pytest.raises(InvalidTaskIdError):
            self.controller.delete_task("0")
    
    def test_delete_nonexistent_task(self):
        """Test deleting a non-existent task."""
        result = self.controller.delete_task("1")
        
        assert result is False
    
    def test_mark_task_status_complete(self):
        """Test marking a task as complete."""
        task = self.controller.add_task("Test task")
        assert task.completed is False
        
        updated_task = self.controller.mark_task_status("1", "complete")
        
        assert updated_task.completed is True
    
    def test_mark_task_status_incomplete(self):
        """Test marking a task as incomplete."""
        task = self.controller.add_task("Test task")
        # Mark as complete first
        self.controller.mark_task_status("1", "complete")
        
        # Now mark as incomplete
        updated_task = self.controller.mark_task_status("1", "incomplete")
        
        assert updated_task.completed is False
    
    def test_mark_task_status_invalid_status(self):
        """Test that using an invalid status raises ValueError."""
        self.controller.add_task("Test task")
        
        with pytest.raises(ValueError):
            self.controller.mark_task_status("1", "invalid_status")
    
    def test_mark_task_status_invalid_id(self):
        """Test that marking status with invalid ID raises InvalidTaskIdError."""
        with pytest.raises(InvalidTaskIdError):
            self.controller.mark_task_status("invalid", "complete")
    
    def test_mark_task_status_nonexistent(self):
        """Test marking status of a non-existent task raises KeyError."""
        with pytest.raises(KeyError):
            self.controller.mark_task_status("1", "complete")
    
    def test_task_exists(self):
        """Test checking if a task exists."""
        task = self.controller.add_task("Test task")
        
        assert self.controller.task_exists("1") is True
        assert self.controller.task_exists("2") is False
    
    def test_task_exists_invalid_id(self):
        """Test that checking existence with invalid ID raises InvalidTaskIdError."""
        with pytest.raises(InvalidTaskIdError):
            self.controller.task_exists("invalid")
        
        with pytest.raises(InvalidTaskIdError):
            self.controller.task_exists("0")