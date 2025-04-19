# Bookstore API Integration Exercise

This folder contains a project where you need to build a client application that integrates with a RESTful Bookstore API service.

## Project Overview

The Bookstore API is a simple RESTful service that allows users to manage a collection of books. Your task is to complete the client application that interacts with this API to perform various operations.

## Components

1. **Bookstore API Service** (`bookstore_api/`):
   - A Flask application that provides RESTful endpoints for book management
   - Simulates a real-world API with proper error handling and responses
   - Runs on localhost:5000

2. **Bookstore Client** (`bookstore_client/`):
   - A partially implemented client application
   - You will need to complete the missing functionality

## Requirements

Your task is to complete the client application to meet the following requirements:

1. **Basic Functionality**:
   - List all books in the bookstore
   - Get details of a specific book by ID
   - Add a new book to the bookstore
   - Update an existing book's information
   - Delete a book from the bookstore
   - Search for books by title or author

2. **Error Handling**:
   - Implement proper error handling for API responses
   - Display user-friendly error messages
   - Handle network connectivity issues

3. **User Experience**:
   - Provide clear feedback on operation success/failure
   - Implement input validation before sending requests
   - Display data in a formatted, easy-to-read manner

## Getting Started

1. **Set up the environment**:
   ```bash
   # Navigate to the project directory
   cd P4_integration
   
   # Create a virtual environment (optional but recommended)
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   
   # Install dependencies
   pip install -r requirements.txt
   ```

2. **Start the Bookstore API service**:
   ```bash
   # In one terminal
   python bookstore_api/app.py
   ```

3. **Test the client application**:
   ```bash
   # In another terminal
   python bookstore_client/client.py
   ```

## API Documentation

The Bookstore API provides the following endpoints:

| Endpoint                 | Method | Description                       | Request Body                                   | Response                     |
|--------------------------|--------|-----------------------------------|-----------------------------------------------|------------------------------|
| `/api/books`             | GET    | Get all books                     | None                                          | List of books                |
| `/api/books/<id>`        | GET    | Get a specific book               | None                                          | Book details                 |
| `/api/books`             | POST   | Add a new book                    | `{"title": "...", "author": "...", "price": 0.0}` | Created book                 |
| `/api/books/<id>`        | PUT    | Update a book                     | `{"title": "...", "author": "...", "price": 0.0}` | Updated book                 |
| `/api/books/<id>`        | DELETE | Delete a book                     | None                                          | Success message              |
| `/api/books/search`      | GET    | Search books by title or author   | Query params: `?query=...`                    | List of matching books       |

## Assessment Criteria

Your implementation will be assessed on:
1. Correctness of the implementation
2. Error handling and edge cases
3. Code organization and structure
4. User experience and feedback
5. Documentation and comments
