# FastAPI CRUD MySQL Application

A FastAPI-based REST API application with MySQL database integration, featuring JWT authentication, correlation ID tracking, and comprehensive logging.

## Features

- **CRUD Operations**: Complete user management with Create, Read, Update, Delete operations
- **JWT Authentication**: Secure API endpoints with Bearer token authentication
- **Correlation ID Tracking**: Request tracing across the application
- **Structured Logging**: Comprehensive logging with correlation ID integration
- **Exception Handling**: Custom exception handlers for better error responses
- **Database Integration**: MySQL database with SQLModel ORM

## Project Structure

    ```
    fastapi-crud-mysql/
    ├── app/
    │   ├── core/
    │   │   ├── context/
    │   │   │   └── context.py          # Correlation ID context management
    │   │   ├── security/
    │   │   │   └── security.py         # JWT token creation and verification
    │   │   ├── config.py               # Application configuration
    │   │   └── logging_config.py       # Logging configuration
    │   ├── db/
    │   │   └── session.py              # Database session management
    │   ├── dependencies/
    │   │   └── auth.py                 # Authentication dependencies
    │   ├── exceptions/
    │   │   ├── custom_exceptions.py    # Custom exception classes
    │   │   └── handlers.py             # Exception handlers
    │   ├── middleware/
    │   │   ├── correlation_middleware.py # Correlation ID middleware
    │   │   └── logging_middleware.py   # Request logging middleware
    │   ├── models/
    │   │   ├── user_model.py           # User database model
    │   │   └── login_request_model.py  # Login request model
    │   ├── repositories/
    │   │   └── user_repo.py            # User repository layer
    │   ├── routes/
    │   │   └── user_routes.py          # User API routes
    │   ├── services/
    │   │   └── user_service.py         # User business logic
    │   └── main.py                     # Application entry point
    └── README.md
    ```

## Prerequisites

- Python 3.10+
- MySQL Server
- pip (Python package manager)

## Setup Instructions

### 1. Clone the Repository

    ```bash
    git clone https://github.com/zeeshanalamkhan/fastapi-crud-mysql
    cd fastapi-crud-mysql
    ```

### 2. Create Virtual Environment

    ```bash
    python -m venv venv
    venv\Scripts\activate  # On Windows
    # source venv/bin/activate  # On macOS/Linux
    ```

### 3. Install Dependencies

    ```bash
    pip install fastapi uvicorn sqlmodel pymysql python-jose[cryptography] python-multipart PyMySQL PyJWT
    ```

### 4. Database Setup

1. **Create MySQL Database:**
    ```sql
    CREATE DATABASE user_db;
    ```

2. **Update Database Configuration:**
   Edit [config.py](app/core/config.py) if needed:
    ```python
    DATABASE_URL = "mysql+pymysql://root:root@localhost:3306/user_db"
    ```

### 5. Run the Application

    ```bash
    uvicorn app.main:app --reload --port 8001
    ```

The application will be available at `http://localhost:8001`

## Code Architecture Explanation

### Core Components

#### 1. Configuration ([config.py](app/core/config.py))
Contains application-wide configuration including database URL, JWT settings, and correlation header configuration.

#### 2. Database Layer ([session.py](app/db/session.py))
Manages database connections using SQLModel with MySQL backend.

#### 3. Authentication System
- **Security Module ([security.py](app/core/security/security.py))**: JWT token creation and verification
- **Auth Dependencies ([auth.py](app/dependencies/auth.py))**: Authentication interceptor for protected routes

#### 4. Middleware Stack
- **Correlation Middleware ([correlation_middleware.py](app/middleware/correlation_middleware.py))**: Generates and tracks correlation IDs
- **Logging Middleware ([logging_middleware.py](app/middleware/logging_middleware.py))**: Logs request/response information

#### 5. Logging System ([logging_config.py](app/core/logging_config.py))
Custom logging configuration with correlation ID integration for request tracing.

#### 6. Exception Handling
- **Custom Exceptions ([custom_exceptions.py](app/exceptions/custom_exceptions.py))**: Application-specific exceptions
- **Exception Handlers ([handlers.py](app/exceptions/handlers.py))**: Centralized exception handling

#### 7. Data Layer
- **Models ([user_model.py](app/models/user_model.py))**: SQLModel database models
- **Repository ([user_repo.py](app/repositories/user_repo.py))**: Data access layer
- **Service ([user_service.py](app/services/user_service.py))**: Business logic layer

## API Endpoints

### Authentication
- `POST /auth/token` - Generate JWT token

### User Management (Protected)
- `POST /users` - Create new user
- `GET /users` - Get all users
- `GET /users/{user_id}` - Get user by ID
- `PUT /users` - Update user
- `DELETE /users/{user_id}` - Delete user

## API Usage Examples

### 1. Generate Authentication Token

    ```bash
    curl -X POST "http://localhost:8001/auth/token" \
      -H "Content-Type: application/json" \
      -d '{
        "username": "testuser"
      }'
    ```

**Response:**
    ```json
    {
      "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
      "token_type": "Bearer"
    }
    ```

### 2. Create User

    ```bash
    curl -X POST "http://localhost:8001/users" \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer YOUR_TOKEN_HERE" \
      -H "x-correlation-id: 12345678-1234-1234-1234-123456789abc" \
      -d '{
        "name": "John Doe",
        "email": "john.doe@example.com"
      }'
    ```

**Response:**
    ```json
    {
      "id": 1,
      "name": "John Doe",
      "email": "john.doe@example.com"
    }
    ```

### 3. Get All Users

    ```bash
    curl -X GET "http://localhost:8001/users" \
      -H "Authorization: Bearer YOUR_TOKEN_HERE" \
      -H "x-correlation-id: 12345678-1234-1234-1234-123456789abc"
    ```

**Response:**
    ```json
    [
      {
        "id": 1,
        "name": "John Doe",
        "email": "john.doe@example.com"
      }
    ]
    ```

### 4. Get User by ID

    ```bash
    curl -X GET "http://localhost:8001/users/1" \
      -H "Authorization: Bearer YOUR_TOKEN_HERE" \
      -H "x-correlation-id: 12345678-1234-1234-1234-123456789abc"
    ```

**Response:**
    ```json
    {
      "id": 1,
      "name": "John Doe",
      "email": "john.doe@example.com"
    }
    ```

### 5. Update User

    ```bash
    curl -X PUT "http://localhost:8001/users" \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer YOUR_TOKEN_HERE" \
      -H "x-correlation-id: 12345678-1234-1234-1234-123456789abc" \
      -d '{
        "id": 1,
        "name": "John Smith",
        "email": "john.smith@example.com"
      }'
    ```

**Response:**
    ```json
    {
      "id": 1,
      "name": "John Smith",
      "email": "john.smith@example.com"
    }
    ```

### 6. Delete User

    ```bash
    curl -X DELETE "http://localhost:8001/users/1" \
      -H "Authorization: Bearer YOUR_TOKEN_HERE" \
      -H "x-correlation-id: 12345678-1234-1234-1234-123456789abc"
    ```

**Response:**
    ```json
    {
      "message": "Deleted"
    }
    ```

## Error Responses

### Missing Authorization Header
    ```json
    {
      "message": "Missing Authorization header"
    }
    ```

### Invalid/Expired Token
    ```json
    {
      "message": "Token expired!"
    }
    ```

### User Not Found
    ```json
    {
      "message": "User not found!"
    }
    ```

## Logging and Correlation ID

The application automatically generates correlation IDs for request tracing. You can:

1. **Provide your own correlation ID** in the `x-correlation-id` header
2. **Let the system generate one** automatically if not provided

All logs will include the correlation ID for easy request tracing:

    ```
    [Correlation_Id: 12345678-1234-1234-1234-123456789abc] INFO - Incoming request : GET http://localhost:8001/users
    [Correlation_Id: 12345678-1234-1234-1234-123456789abc] INFO - Fetching all users
    [Correlation_Id: 12345678-1234-1234-1234-123456789abc] INFO - Completed in 0.0234 sec
    ```

## Security Features

- **JWT Authentication**: All user endpoints require valid JWT tokens
- **Token Expiration**: Tokens expire after 10 minutes (configurable)
- **Secure Headers**: Correlation IDs are included in response headers
- **Input Validation**: Pydantic models ensure data validation

## Development

### Running in Development Mode

    ```bash
    uvicorn app.main:app --reload --port 8001
    ```

### Environment Variables

You can override configuration by setting environment variables or modifying [config.py](app/core/config.py):

- `DATABASE_URL`: MySQL connection string
- `SECRET_KEY`: JWT signing key
- `TOKEN_EXPIRE_TIME_MINUTES`: Token expiration time

## Troubleshooting

### Common Issues

1. **Database Connection Error**: Ensure MySQL is running and credentials are correct
2. **Import Errors**: Verify all dependencies are installed
3. **Authentication Errors**: Check token format and expiration
4. **CORS Issues**: Add CORS middleware if accessing from browser

### Logs Location

Application logs are output to the console with correlation ID tracking for easy debugging.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License.