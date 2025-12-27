# Data Model: Phase II Full-Stack Todo Application

## User Entity

**Name**: User
**Description**: Represents an authenticated user of the todo application
**Fields**:
- id: Integer (Primary Key, Auto-increment)
- email: String (Unique, Required, Max length: 255)
- hashed_password: String (Required, Max length: 255)
- created_at: DateTime (Required, Auto-generated)
- updated_at: DateTime (Required, Auto-generated)

**Validation Rules**:
- Email must be a valid email format
- Email must be unique across all users
- Password must meet minimum security requirements (8+ characters)
- Email and password are required for registration

**Relationships**:
- One-to-Many: User has many Todos

## Todo Entity

**Name**: Todo
**Description**: Represents a task/todo item owned by a user
**Fields**:
- id: Integer (Primary Key, Auto-increment)
- title: String (Required, Max length: 255)
- description: Text (Optional)
- completed: Boolean (Default: false)
- user_id: Integer (Foreign Key to User.id, Required)
- created_at: DateTime (Required, Auto-generated)
- updated_at: DateTime (Required, Auto-generated)

**Validation Rules**:
- Title is required
- Title must be between 1 and 255 characters
- Description can be empty
- Completed defaults to false
- user_id must reference an existing User

**Relationships**:
- Many-to-One: Todo belongs to one User
- User has many Todos

## State Transitions

### Todo State Transitions
- **Created**: A new todo is created with `completed = false`
- **Updated**: A todo can be modified (title, description)
- **Completed/Incomplete**: A todo can toggle between completed and incomplete states
- **Deleted**: A todo can be removed from the system

## Database Constraints

- **User**: Email uniqueness constraint
- **Todo**: Foreign key constraint ensuring user_id references a valid User
- **Todo**: Required field constraints on title and user_id

## Indexes

- **User**: Index on email for efficient lookup during authentication
- **Todo**: Index on user_id for efficient retrieval of user's todos
- **Todo**: Composite index on user_id and completed for filtered queries