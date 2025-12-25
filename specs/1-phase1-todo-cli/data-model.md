# Data Model: Phase I - Evolution of Todo CLI Application

**Feature**: Phase I - Evolution of Todo CLI Application
**Date**: 2025-01-01
**Plan**: [link to plan.md]

## Task Entity

### Attributes
- **id**: Integer, unique identifier for the task (auto-incremented)
- **description**: String, the task description (required, non-empty)
- **completed**: Boolean, completion status (default: False)

### Implementation
```python
class Task:
    def __init__(self, id: int, description: str, completed: bool = False):
        self.id = id
        self.description = description
        self.completed = completed
```

## In-Memory Storage

### Task Storage Structure
- **tasks**: Dictionary mapping task ID (int) to Task objects
- **next_id**: Integer counter for generating unique task IDs

### Operations
- **Create**: Add new Task object to tasks dict with new ID
- **Read**: Retrieve Task object by ID from tasks dict
- **Update**: Modify Task object attributes in tasks dict
- **Delete**: Remove Task object from tasks dict by ID

## Constraints
- Task descriptions must not be empty strings
- Task IDs must be unique within the application session
- Task IDs are auto-generated using an incrementing counter