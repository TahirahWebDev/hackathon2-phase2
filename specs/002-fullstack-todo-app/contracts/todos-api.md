# API Contracts: Phase II Full-Stack Todo Application

## Authentication Endpoints

### POST /api/auth/signup
**Purpose**: Register a new user account
**Request Body**:
```json
{
  "email": "string (required)",
  "password": "string (required, min 8 characters)"
}
```
**Response**:
- 201 Created: User successfully registered
```json
{
  "id": "integer",
  "email": "string",
  "created_at": "datetime"
}
```
- 400 Bad Request: Invalid input
- 409 Conflict: Email already exists

### POST /api/auth/signin
**Purpose**: Authenticate an existing user
**Request Body**:
```json
{
  "email": "string (required)",
  "password": "string (required)"
}
```
**Response**:
- 200 OK: User successfully authenticated
```json
{
  "access_token": "string",
  "token_type": "string",
  "user": {
    "id": "integer",
    "email": "string"
  }
}
```
- 401 Unauthorized: Invalid credentials

### POST /api/auth/signout
**Purpose**: Log out the current user
**Headers**: Authorization: Bearer {token}
**Response**:
- 200 OK: User successfully logged out
- 401 Unauthorized: Invalid token

## Todo Management Endpoints

### GET /api/todos
**Purpose**: Retrieve all todos for the authenticated user
**Headers**: Authorization: Bearer {token}
**Response**:
- 200 OK: List of todos
```json
[
  {
    "id": "integer",
    "title": "string",
    "description": "string",
    "completed": "boolean",
    "user_id": "integer",
    "created_at": "datetime",
    "updated_at": "datetime"
  }
]
```
- 401 Unauthorized: Invalid token

### POST /api/todos
**Purpose**: Create a new todo for the authenticated user
**Headers**: Authorization: Bearer {token}
**Request Body**:
```json
{
  "title": "string (required)",
  "description": "string (optional)",
  "completed": "boolean (optional, default false)"
}
```
**Response**:
- 201 Created: Todo successfully created
```json
{
  "id": "integer",
  "title": "string",
  "description": "string",
  "completed": "boolean",
  "user_id": "integer",
  "created_at": "datetime",
  "updated_at": "datetime"
}
```
- 400 Bad Request: Invalid input
- 401 Unauthorized: Invalid token

### GET /api/todos/{id}
**Purpose**: Retrieve a specific todo by ID
**Headers**: Authorization: Bearer {token}
**Path Parameter**: id (integer, required)
**Response**:
- 200 OK: Todo details
```json
{
  "id": "integer",
  "title": "string",
  "description": "string",
  "completed": "boolean",
  "user_id": "integer",
  "created_at": "datetime",
  "updated_at": "datetime"
}
```
- 401 Unauthorized: Invalid token
- 404 Not Found: Todo doesn't exist or doesn't belong to user

### PUT /api/todos/{id}
**Purpose**: Update an existing todo
**Headers**: Authorization: Bearer {token}
**Path Parameter**: id (integer, required)
**Request Body**:
```json
{
  "title": "string (optional)",
  "description": "string (optional)",
  "completed": "boolean (optional)"
}
```
**Response**:
- 200 OK: Todo successfully updated
```json
{
  "id": "integer",
  "title": "string",
  "description": "string",
  "completed": "boolean",
  "user_id": "integer",
  "created_at": "datetime",
  "updated_at": "datetime"
}
```
- 400 Bad Request: Invalid input
- 401 Unauthorized: Invalid token
- 404 Not Found: Todo doesn't exist or doesn't belong to user

### PATCH /api/todos/{id}/toggle
**Purpose**: Toggle the completion status of a todo
**Headers**: Authorization: Bearer {token}
**Path Parameter**: id (integer, required)
**Response**:
- 200 OK: Todo completion status updated
```json
{
  "id": "integer",
  "title": "string",
  "description": "string",
  "completed": "boolean",
  "user_id": "integer",
  "created_at": "datetime",
  "updated_at": "datetime"
}
```
- 401 Unauthorized: Invalid token
- 404 Not Found: Todo doesn't exist or doesn't belong to user

### DELETE /api/todos/{id}
**Purpose**: Delete a specific todo
**Headers**: Authorization: Bearer {token}
**Path Parameter**: id (integer, required)
**Response**:
- 204 No Content: Todo successfully deleted
- 401 Unauthorized: Invalid token
- 404 Not Found: Todo doesn't exist or doesn't belong to user