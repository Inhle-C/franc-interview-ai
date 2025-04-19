#!/usr/bin/env python3
"""
Bookstore API

A RESTful Flask application that provides endpoints to manage books.
"""
from flask import Flask, jsonify, request, abort
from flask_cors import CORS
import json
import os
import time
import uuid

app = Flask(__name__)
CORS(app)  # Enable Cross-Origin Resource Sharing

# Data file to persist books
DATA_FILE = os.path.join(os.path.dirname(__file__), 'books.json')

# Initialize with some sample books if the file doesn't exist
SAMPLE_BOOKS = [
    {
        "id": "1",
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "price": 12.99,
        "in_stock": True
    },
    {
        "id": "2",
        "title": "1984",
        "author": "George Orwell",
        "price": 10.99,
        "in_stock": True
    },
    {
        "id": "3",
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "price": 11.50,
        "in_stock": False
    }
]


def load_books():
    """Load books from the data file."""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    else:
        # Initialize with sample books if file doesn't exist
        save_books(SAMPLE_BOOKS)
        return SAMPLE_BOOKS


def save_books(books):
    """Save books to the data file."""
    with open(DATA_FILE, 'w') as f:
        json.dump(books, f, indent=2)


@app.route('/api/books', methods=['GET'])
def get_books():
    """Get all books endpoint."""
    # Simulate network delay for realistic API behavior
    time.sleep(0.2)
    
    books = load_books()
    return jsonify(books)


@app.route('/api/books/<book_id>', methods=['GET'])
def get_book(book_id):
    """Get a specific book by ID."""
    # Simulate network delay
    time.sleep(0.2)
    
    books = load_books()
    book = next((b for b in books if b['id'] == book_id), None)
    
    if book:
        return jsonify(book)
    else:
        abort(404, description="Book not found")


@app.route('/api/books', methods=['POST'])
def add_book():
    """Add a new book."""
    # Simulate network delay
    time.sleep(0.5)
    
    if not request.json:
        abort(400, description="Request must be JSON")
    
    data = request.json
    
    # Validate required fields
    if not all(k in data for k in ('title', 'author', 'price')):
        abort(400, description="Missing required fields: title, author, price")
    
    # Create new book
    new_book = {
        'id': str(uuid.uuid4())[:8],  # Generate a short unique ID
        'title': data['title'],
        'author': data['author'],
        'price': float(data['price']),
        'in_stock': data.get('in_stock', True)
    }
    
    books = load_books()
    books.append(new_book)
    save_books(books)
    
    return jsonify(new_book), 201


@app.route('/api/books/<book_id>', methods=['PUT'])
def update_book(book_id):
    """Update an existing book."""
    # Simulate network delay
    time.sleep(0.5)
    
    if not request.json:
        abort(400, description="Request must be JSON")
    
    books = load_books()
    book = next((b for b in books if b['id'] == book_id), None)
    
    if not book:
        abort(404, description="Book not found")
    
    data = request.json
    
    # Update book fields if provided
    book['title'] = data.get('title', book['title'])
    book['author'] = data.get('author', book['author'])
    book['price'] = float(data.get('price', book['price']))
    book['in_stock'] = data.get('in_stock', book['in_stock'])
    
    save_books(books)
    
    return jsonify(book)


@app.route('/api/books/<book_id>', methods=['DELETE'])
def delete_book(book_id):
    """Delete a book."""
    # Simulate network delay
    time.sleep(0.5)
    
    books = load_books()
    book = next((b for b in books if b['id'] == book_id), None)
    
    if not book:
        abort(404, description="Book not found")
    
    books = [b for b in books if b['id'] != book_id]
    save_books(books)
    
    return jsonify({'message': f"Book with ID {book_id} deleted successfully"})


@app.route('/api/books/search', methods=['GET'])
def search_books():
    """Search for books by title or author."""
    # Simulate network delay
    time.sleep(0.3)
    
    query = request.args.get('query', '').lower()
    
    if not query:
        abort(400, description="Search query is required")
    
    books = load_books()
    results = [
        book for book in books
        if query in book['title'].lower() or query in book['author'].lower()
    ]
    
    return jsonify(results)


@app.errorhandler(400)
def bad_request(error):
    """Handle bad request errors."""
    return jsonify({'error': 'Bad Request', 'message': error.description}), 400


@app.errorhandler(404)
def not_found(error):
    """Handle not found errors."""
    return jsonify({'error': 'Not Found', 'message': error.description}), 404


@app.errorhandler(500)
def server_error(error):
    """Handle internal server errors."""
    return jsonify({'error': 'Internal Server Error', 'message': str(error)}), 500


if __name__ == '__main__':
    if not os.path.exists(os.path.dirname(DATA_FILE)):
        os.makedirs(os.path.dirname(DATA_FILE))
    
    # Ensure we have the books.json file
    if not os.path.exists(DATA_FILE):
        save_books(SAMPLE_BOOKS)
    
    print("Bookstore API running on http://localhost:5000")
    app.run(debug=True) 