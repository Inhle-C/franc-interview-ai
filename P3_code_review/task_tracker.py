#!/usr/bin/env python3
"""
Task Tracker Application

A simple console application for tracking tasks.
"""
import json
import os
from datetime import datetime
import time

# Global variables
TASKS_FILE = "tasks.json"
tasks = {}
# Counter for last used ID
LAST_ID_FILE = "last_id.txt"

def load_tasks():
    """Load tasks from the JSON file."""
    global tasks
    if os.path.exists(TASKS_FILE):
        try:
            with open(TASKS_FILE, "r") as f:
                tasks = json.load(f)
                save_tasks()
        except json.JSONDecodeError:
            # Old Bug: Silent failure on corrupted JSON, doesn't initialize 'tasks'
            print("Warning: Tasks file is corrupted.")
            # Missing: Should initialize tasks = {} here
            tasks = {}
            save_tasks()
    else:
        # Create an empty JSON file if it doesn't exist
        save_tasks()

def save_tasks():
    """Save tasks to the JSON file."""
    #Old Bug: No error handling for file operations
    try:
        with open(TASKS_FILE, "w") as f:
            json.dump(tasks, f)
    except IOError as e:
        print(f"Error saving tasks: {e}")

#new method
def validate_date(date_str):
    try:
        date = datetime.strptime(date_str, "%Y-%m-%d")
        if date < datetime.now():
            print("Due date must be in the future.")
            return None
        return date_str
    except ValueError:
        print("Invalid date format. Use YYYY-MM-DD.")
        return None
    
def generate_task_id():
    """Generate a new unique task ID."""
    # Old Bug: This doesn't guarantee uniqueness if tasks are deleted
    last_id = 0
    if os.path.exists(LAST_ID_FILE):
        with open(LAST_ID_FILE, "r") as f:
            try:
                last_id = int(f.read().strip())
            except ValueError:
                last_id = 0
    last_id += 1
    with open(LAST_ID_FILE, "w") as f:
        f.write(str(last_id))
    return str(last_id)


def add_task():
    """Add a new task."""
    print("\n=== Add New Task ===")
    
    title = input("Enter task title: ").strip()
    # Old Bug: Missing validation for empty title
    if not title:
        print("Title cannot be empty.")
        return
    
    description = input("Enter task description: ").strip()
    
    # Old Bug: No validation or error handling for date format
    # Missing: No validation that the date is in the future
    while True:
        due_date_input = input("Enter due date (YYYY-MM-DD): ").strip()
        due_date = validate_date(due_date_input)
        if due_date:
            break 
    
    task_id = str(generate_task_id())
    tasks[task_id] = {
        "title": title,
        "description": description,
        "due_date": due_date,
        "status": "incomplete",
        # Old Bug: Missing created_date field required by specs
        "created_date": datetime.now().strftime("%Y-%m-%d")
    }
    
    save_tasks()
    print(f"Task {task_id} added successfully!")

def view_all_tasks():
    """View all tasks."""
    print("\n=== All Tasks ===")
    
    if not tasks:
        print("No tasks found.")
        return
    
    # Old Bug: This doesn't format output nicely with proper spacing
    print(f"{'ID':<10} {'Title':<25} {'Due Date':<15} {'Status':<10}")
    print("-" * 40)
    for task_id, task in tasks.items():
        print(f"{task_id:<10} {task['title']:<25} {task['due_date']:<15} {task['status']:<10}")


def view_task():
    """View details of a specific task."""
    print("\n=== View Task ===")
    
    task_id = input("Enter task ID: ")
    #Old Bug: Missing validation for non-existent task IDs
    if not task_id.isnumeric() or int(task_id)<=0:
        print(f"TaskID requeries a positive real number")
        return
    
    if task_id not in tasks:
        print(f"Task {task_id} not found.")
        return
    
    task = tasks[task_id]
    print(f"ID: {task_id}")
    print(f"Title: {task['title']}")
    print(f"Description: {task['description']}")
    print(f"Due Date: {task['due_date']}")
    print(f"Status: {task['status']}")

def update_task():
    """Update an existing task."""
    print("\n=== Update Task ===")
    
    task_id = input("Enter task ID: ")

    #Old Bug: Missing validation for non-existent task IDs
    if not task_id.isnumeric() or int(task_id) <= 0:
        print(f"TaskID requeries a positive real number")
        return
    
    if task_id not in tasks:
        print(f"Task {task_id} not found.")
        return
    
    task = tasks[task_id]
    
    print("Leave field empty to keep current value.")
    print(f"Current Title: {task['title']}")
    new_title = input("New Title: ")
    
    print(f"Current Description: {task['description']}")
    new_description = input("New Description: ")
    
    print(f"Current Due Date: {task['due_date']}")
    new_due = input("New Due Date (YYYY-MM-DD): ").strip()
    
    #Old Bug: No validation on due date format
    new_due_date = validate_date(new_due) if new_due else task['due_date']
    
    # Update task with new values, keeping old values if input is empty
    if new_title:
        task['title'] = new_title
    if new_description:
        task['description'] = new_description
    if new_due_date:
        # Bug: No validation of date format
        task['due_date'] = new_due_date
    
    save_tasks()
    print(f"Task {task_id} updated successfully!")

# Bug: Missing implementation of mark_task_complete function (FR1.7)
def mark_task_complete():
    task_id = input("Enter task ID to mark as complete: ").strip()
    task = tasks.get(task_id)
    if not task:
        print(f"Task {task_id} not found.")
        return
    if task['status'] == 'complete':
        print("Task is already complete.")
        return
    task['status'] = 'complete'
    save_tasks()
    print(f"Task {task_id} marked as complete.")
    

def delete_task():
    """Delete a task."""
    print("\n=== Delete Task ===")
    
    task_id = input("Enter task ID: ").strip()
    
    if task_id not in tasks:
        print(f"Task {task_id} not found.")
        return
    
    #Old Bug: Missing confirmation before deletion
    confirm = input("Are you sure you want to delete this task? (y/n): ").lower()
    if confirm != 'y':
        print("Deletion cancelled.")
        return
    del tasks[task_id]
    save_tasks()
    print(f"Task {task_id} deleted successfully!")

def display_menu():
    """Display the main menu."""
    print("\n=== Task Tracker ===")
    print("1. Add Task")
    print("2. View All Tasks")
    print("3. View Task")
    print("4. Update Task")
    # Bug: Missing option for marking task as complete
    print("5. Mark Task Complete")
    print("6. Delete Task")
    print("7. Exit")

def main():
    """Main application function."""
    load_tasks()
    
    while True:
        display_menu()
        
        # Bug: No validation on choice input
        choice = input("Enter your choice (1-7): ").strip()
        while not choice.isnumeric() or not (1<=int(choice)<=7):
            print("Invalid choice. Please try again.")
            choice = input("Enter your choice (1-7): ").strip()
        
        if choice == "1":
            add_task()
        elif choice == "2":
            view_all_tasks()
        elif choice == "3":
            view_task()
        elif choice == "4":
            update_task()
        elif choice == "5":
            mark_task_complete()
        elif choice == "6":
            delete_task()
        elif choice == "7":
            print("Exiting Task Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main() 