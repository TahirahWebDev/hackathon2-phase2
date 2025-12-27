# Phase II Full-Stack Todo Application

This is the implementation of the Phase II todo application, featuring a Next.js frontend with user authentication and a Python REST API backend.

## Features

- User authentication (signup/signin)
- Todo management (create, read, update, delete, mark complete/incomplete)
- Data persistence in Neon Serverless PostgreSQL
- Responsive UI for desktop and mobile

## Tech Stack

- **Backend**: Python, FastAPI, SQLModel, Neon Serverless PostgreSQL
- **Frontend**: Next.js, React, TypeScript
- **Authentication**: JWT-based authentication
- **Styling**: Tailwind CSS

## Setup

### Prerequisites

- Python 3.11+
- Node.js 18+
- npm or yarn
- Neon Serverless PostgreSQL account

### Backend Setup

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -e .
   ```

4. Set up environment variables:
   ```bash
   cp .env.example .env
   # Edit .env file with your Neon PostgreSQL connection details and other configurations
   ```

5. Run the application:
   ```bash
   uvicorn src.api.main:app --reload
   ```

### Frontend Setup

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   # or
   yarn install
   ```

3. Set up environment variables:
   ```bash
   cp .env.example .env
   # Edit .env file with your backend API URL and other configurations
   ```

4. Run the development server:
   ```bash
   npm run dev
   # or
   yarn dev
   ```

## API Documentation

Backend API documentation is available at `http://localhost:8000/docs` when the backend is running.