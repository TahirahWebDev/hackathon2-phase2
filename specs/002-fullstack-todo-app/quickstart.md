# Quickstart Guide: Phase II Full-Stack Todo Application

## Prerequisites

- Python 3.11+
- Node.js 18+
- npm or yarn
- Neon Serverless PostgreSQL account
- Git

## Setup Instructions

### 1. Clone the Repository
```bash
git clone <repository-url>
cd <repository-name>
```

### 2. Backend Setup
```bash
# Navigate to backend directory
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env file with your Neon PostgreSQL connection details and other configurations
```

### 3. Frontend Setup
```bash
# Navigate to frontend directory
cd frontend

# Install dependencies
npm install
# or
yarn install

# Set up environment variables
cp .env.example .env
# Edit .env file with your backend API URL and other configurations
```

### 4. Database Setup
```bash
# From the backend directory with virtual environment activated
cd backend

# Run database migrations
python -m src.database.migrate
```

### 5. Running the Application

#### Backend
```bash
# From the backend directory with virtual environment activated
cd backend
python -m src.api.main
```

#### Frontend
```bash
# From the frontend directory
cd frontend
npm run dev
# or
yarn dev
```

## API Documentation
- Backend API documentation will be available at `http://localhost:8000/docs` when the backend is running
- The API follows the contracts defined in `specs/002-fullstack-todo-app/contracts/`

## Testing
### Backend Tests
```bash
# From the backend directory
cd backend
pytest
```

### Frontend Tests
```bash
# From the frontend directory
cd frontend
npm run test
# or
yarn test
```

## Environment Variables

### Backend (.env)
- `DATABASE_URL`: Neon Serverless PostgreSQL connection string
- `SECRET_KEY`: Secret key for JWT token generation
- `ALGORITHM`: Algorithm for JWT encoding (default: HS256)
- `ACCESS_TOKEN_EXPIRE_MINUTES`: Token expiration time in minutes

### Frontend (.env)
- `NEXT_PUBLIC_API_URL`: URL of the backend API (e.g., http://localhost:8000)