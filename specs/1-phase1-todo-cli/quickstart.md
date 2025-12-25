# Quickstart Guide: Phase I - Evolution of Todo CLI Application

**Feature**: Phase I - Evolution of Todo CLI Application
**Date**: 2025-01-01
**Plan**: [link to plan.md]

## Running the Application

1. Ensure Python 3.8+ is installed on your system
2. Navigate to the project root directory
3. Run the application:
   ```bash
   python -m src.todo_app.main
   ```
   
## Using the Application

When the application starts, you'll see a menu with the following options:

```
Todo App Menu:
1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Mark Task Complete/Incomplete
6. Exit
```

### Adding a Task
1. Select option 1
2. Enter the task description when prompted
3. The task will be added with a unique ID

### Viewing Tasks
1. Select option 2
2. All tasks will be displayed with their ID, description, and completion status

### Updating a Task
1. Select option 3
2. Enter the task ID you want to update
3. Enter the new task description

### Deleting a Task
1. Select option 4
2. Enter the task ID you want to delete
3. The task will be removed from the list

### Marking Task Complete/Incomplete
1. Select option 5
2. Enter the task ID you want to modify
3. Enter 'complete' or 'incomplete' to set the status

### Exiting
1. Select option 6 to exit the application
2. Note: All tasks will be lost when the application exits (in-memory only)