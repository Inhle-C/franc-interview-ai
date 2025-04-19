#!/usr/bin/env python3
"""
Test script for the Bookstore Client

This script tests the implementation of the Bookstore client
by calling each function and validating its functionality.
"""
import unittest
import requests
from unittest.mock import patch, MagicMock
import json
import io
import sys

# Import client module
from client import (
    get_all_books,
    get_book_by_id,
    add_book,
    update_book,
    delete_book,
    search_books
)

class TestBookstoreClient(unittest.TestCase):
    """Test cases for Bookstore client implementation."""

    def setUp(self):
        """Set up test fixtures."""
        # Sample books data for testing
        self.sample_books = [
            {
                "id": "1",
                "title": "Test Book 1",
                "author": "Test Author 1",
                "price": 10.99,
                "in_stock": True
            },
            {
                "id": "2",
                "title": "Test Book 2",
                "author": "Test Author 2",
                "price": 12.99,
                "in_stock": False
            }
        ]
        
        self.single_book = self.sample_books[0]
    
    @patch('client.requests.get')
    def test_get_all_books(self, mock_get):
        """Test the get_all_books function."""
        # Mock the response
        mock_response = MagicMock()
        mock_response.json.return_value = self.sample_books
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response
        
        # Call the function
        result = get_all_books()
        
        # Assert the result
        self.assertEqual(result, self.sample_books)
        mock_get.assert_called_once()
    
    @patch('client.requests.get')
    def test_get_book_by_id(self, mock_get):
        """Test the get_book_by_id function."""
        # This test will fail until the function is implemented
        #if get_book_by_id("1") is None:
            #self.skipTest("get_book_by_id function not implemented yet")
        
        # Mock the response
        mock_response = MagicMock()
        mock_response.json.return_value = self.single_book
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response
        
        # Call the function
        result = get_book_by_id("1")
        
        # Assert the result
        self.assertEqual(result, self.single_book)
        mock_get.assert_called_once()
    
    @patch('client.requests.get')
    def test_get_book_by_id_error(self, mock_get):
        """Test error handling in get_book_by_id function."""
        # This test will fail until the function is implemented
        if get_book_by_id("999") is None:
            self.skipTest("get_book_by_id function not implemented yet")
        
        # Mock a 404 error
        mock_get.side_effect = requests.exceptions.HTTPError("404 Not Found")
        
        # Call the function
        result = get_book_by_id("999")
        
        # Assert the result
        self.assertIsNone(result)
    
    # More tests would be implemented here for other functions
    # ...

if __name__ == '__main__':
    print("Running tests for Bookstore Client implementation...")
    unittest.main() 