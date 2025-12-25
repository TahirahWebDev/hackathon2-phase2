"""
Integration tests for the Todo CLI application flow.
Tests the interaction between different components.
"""
import pytest
from src.todo_app.controllers import TodoController
from src.todo_app.utils import InvalidTaskIdError, EmptyTaskDescriptionError


class TestAppFlow:
    """Integration tests for the complete application flow."""
    
    def setup_method(self):
        """Set up a fresh controller for each test."""
        self.controller = TodoController()
    
    def test_complete_user_story_1_add_task(self):
        """Test the complete flow for adding a new task (User Story 1)."""
        # Given: Empty task list
        assert len(self.controller.get_all_tasks()) == 0
        
        # When: User adds a new task with a valid description
        task = self.controller.add_task("Buy groceries")
        
        # Then: The task appears in the task list with a unique ID and status "incomplete"
        assert task.id == 1
        assert task.description == "Buy groceries"
        assert task.completed is False
        
        # And: The task is retrievable from the list
        all_tasks = self.controller.get_all_tasks()
        assert len(all_tasks) == 1
        assert all_tasks[0] == task
    
    def test_complete_user_story_1_add_task_to_existing_list(self):
        """Test adding a task to an existing list (User Story 1)."""
        # Given: Task list with existing tasks
        existing_task = self.controller.add_task("First task")
        assert len(self.controller.get_all_tasks()) == 1
        
        # When: User adds a new task with a valid description
        new_task = self.controller.add_task("Second task")
        
        # Then: The new task appears in the task list with a unique ID and status "incomplete"
        assert new_task.id == 2  # Should get the next ID
        assert new_task.description == "Second task"
        assert new_task.completed is False
        
        # And: Both tasks are in the list
        all_tasks = self.controller.get_all_tasks()
        assert len(all_tasks) == 2
        assert existing_task in all_tasks
        assert new_task in all_tasks
    
    def test_complete_user_story_1_add_task_empty_description(self):
        """Test attempting to add a task with empty description (User Story 1)."""
        # Given: Any task list state
        # When: User attempts to add a task with an empty description
        # Then: The system should raise an error and not add the task
        with pytest.raises(EmptyTaskDescriptionError):
            self.controller.add_task("")
        
        # And: The task list remains empty
        assert len(self.controller.get_all_tasks()) == 0
    
    def test_complete_user_story_2_view_task_list_with_tasks(self):
        """Test viewing a task list with multiple tasks (User Story 2)."""
        # Given: A task list with multiple tasks
        task1 = self.controller.add_task("First task")
        task2 = self.controller.add_task("Task 2")
        task3 = self.controller.add_task("Task 3")

        # When: User requests to view the task list
        all_tasks = self.controller.get_all_tasks()

        # Then: All tasks are returned with their ID, description, and completion status
        assert len(all_tasks) == 3
        assert task1 in all_tasks
        assert task2 in all_tasks
        assert task3 in all_tasks

        # Verify each task has correct attributes
        for i, task in enumerate([task1, task2, task3], 1):
            assert task.id == i
            expected_description = f"Task {i}" if i > 1 else "First task"
            assert task.description == expected_description
            assert task.completed is False
    
    def test_complete_user_story_2_view_empty_task_list(self):
        """Test viewing an empty task list (User Story 2)."""
        # Given: An empty task list
        assert len(self.controller.get_all_tasks()) == 0
        
        # When: User requests to view the task list
        all_tasks = self.controller.get_all_tasks()
        
        # Then: An empty list is returned
        assert len(all_tasks) == 0
    
    def test_complete_user_story_2_view_task_list_with_mixed_status(self):
        """Test viewing a task list with both complete and incomplete tasks (User Story 2)."""
        # Given: A task list with both complete and incomplete tasks
        incomplete_task = self.controller.add_task("Incomplete task")
        complete_task = self.controller.add_task("Complete task")
        
        # Mark one task as complete
        self.controller.mark_task_status("2", "complete")
        
        # When: User requests to view the task list
        all_tasks = self.controller.get_all_tasks()
        
        # Then: All tasks are displayed with clear indication of their completion status
        assert len(all_tasks) == 2
        
        # Find tasks by ID to verify status
        task_by_id = {task.id: task for task in all_tasks}
        assert task_by_id[1].completed is False  # First task should be incomplete
        assert task_by_id[2].completed is True   # Second task should be complete
    
    def test_complete_user_story_3_update_task_description(self):
        """Test updating the description of an existing task (User Story 3)."""
        # Given: A task list with existing tasks
        original_task = self.controller.add_task("Original description")
        assert len(self.controller.get_all_tasks()) == 1
        
        # When: User updates the description of a task with a valid ID
        updated_task = self.controller.update_task("1", "Updated description")
        
        # Then: The task's description is updated in the list
        assert updated_task.id == 1
        assert updated_task.description == "Updated description"
        assert updated_task.completed is False  # Status should remain unchanged
        
        # And: The task can be retrieved with the new description
        retrieved_task = self.controller.get_all_tasks()[0]
        assert retrieved_task.description == "Updated description"
    
    def test_complete_user_story_3_update_task_invalid_id(self):
        """Test attempting to update a task with an invalid/nonexistent ID (User Story 3)."""
        # Given: A task list with existing tasks
        existing_task = self.controller.add_task("Existing task")
        
        # When: User attempts to update a task with an invalid/nonexistent ID
        # Then: The system should raise an error and not modify any tasks
        with pytest.raises(KeyError):
            self.controller.update_task("999", "New description")
        
        # And: The existing task remains unchanged
        tasks = self.controller.get_all_tasks()
        assert len(tasks) == 1
        assert tasks[0].id == 1
        assert tasks[0].description == "Existing task"
    
    def test_complete_user_story_3_update_task_empty_description(self):
        """Test attempting to update a task with an empty description (User Story 3)."""
        # Given: A task list with existing tasks
        existing_task = self.controller.add_task("Original description")
        
        # When: User attempts to update a task with an empty description
        # Then: The system should raise an error and not modify the task
        with pytest.raises(EmptyTaskDescriptionError):
            self.controller.update_task("1", "")
        
        # And: The existing task remains unchanged
        tasks = self.controller.get_all_tasks()
        assert len(tasks) == 1
        assert tasks[0].description == "Original description"
    
    def test_complete_user_story_4_delete_task(self):
        """Test deleting a task by its ID (User Story 4)."""
        # Given: A task list with multiple tasks
        task1 = self.controller.add_task("First task")
        task2 = self.controller.add_task("Second task")
        task3 = self.controller.add_task("Third task")
        assert len(self.controller.get_all_tasks()) == 3
        
        # When: User deletes a task with a valid ID
        result = self.controller.delete_task("2")
        
        # Then: The task is removed from the list
        assert result is True
        remaining_tasks = self.controller.get_all_tasks()
        assert len(remaining_tasks) == 2
        assert task1 in remaining_tasks
        assert task3 in remaining_tasks
        assert task2 not in remaining_tasks  # This task should be gone
    
    def test_complete_user_story_4_delete_task_invalid_id(self):
        """Test attempting to delete a task with an invalid/nonexistent ID (User Story 4)."""
        # Given: A task list with existing tasks
        existing_task = self.controller.add_task("Existing task")
        assert len(self.controller.get_all_tasks()) == 1
        
        # When: User attempts to delete a task with an invalid/nonexistent ID
        result = self.controller.delete_task("999")
        
        # Then: The system should return False and not remove any tasks
        assert result is False
        
        # And: The existing task remains in the list
        tasks = self.controller.get_all_tasks()
        assert len(tasks) == 1
        assert tasks[0].id == 1
        assert tasks[0].description == "Existing task"
    
    def test_complete_user_story_4_delete_last_task(self):
        """Test deleting the last task in the list (User Story 4)."""
        # Given: A task list with one task
        task = self.controller.add_task("Only task")
        assert len(self.controller.get_all_tasks()) == 1
        
        # When: User deletes that task
        result = self.controller.delete_task("1")
        
        # Then: The task is removed and the list becomes empty
        assert result is True
        assert len(self.controller.get_all_tasks()) == 0
    
    def test_complete_user_story_5_mark_task_complete(self):
        """Test marking a task as complete (User Story 5)."""
        # Given: A task list with incomplete tasks
        task = self.controller.add_task("Incomplete task")
        assert task.completed is False
        
        # When: User marks a task as complete
        updated_task = self.controller.mark_task_status("1", "complete")
        
        # Then: The task's status is updated to "complete"
        assert updated_task.completed is True
        assert updated_task.id == 1
        assert updated_task.description == "Incomplete task"
    
    def test_complete_user_story_5_mark_task_incomplete(self):
        """Test marking a task as incomplete (User Story 5)."""
        # Given: A task list with completed tasks
        task = self.controller.add_task("Completed task")
        self.controller.mark_task_status("1", "complete")  # Mark as complete first
        assert task.completed is True
        
        # When: User marks a task as incomplete
        updated_task = self.controller.mark_task_status("1", "incomplete")
        
        # Then: The task's status is updated to "incomplete"
        assert updated_task.completed is False
        assert updated_task.id == 1
        assert updated_task.description == "Completed task"
    
    def test_complete_user_story_5_mark_task_invalid_id(self):
        """Test attempting to change status of a task with an invalid/nonexistent ID (User Story 5)."""
        # Given: A task list with existing tasks
        existing_task = self.controller.add_task("Existing task")
        
        # When: User attempts to change status of a task with an invalid/nonexistent ID
        # Then: The system should raise an error and not modify any tasks
        with pytest.raises(KeyError):
            self.controller.mark_task_status("999", "complete")
        
        # And: The existing task remains unchanged
        tasks = self.controller.get_all_tasks()
        assert len(tasks) == 1
        assert tasks[0].completed is False  # Should still be incomplete