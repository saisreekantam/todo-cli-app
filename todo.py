#!/usr/bin/env python3
"""
To-Do List CLI Application
For students with Roll Number % 2 = 1
"""

import json
import os
from datetime import datetime


class TodoList:
    """A simple to-do list manager"""
    
    def __init__(self, filename="todos.json"):
        """Initialize the to-do list"""
        self.filename = filename
        self.todos = self.load_todos()
    
    def load_todos(self):
        """Load todos from JSON file"""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as f:
                    return json.load(f)
            except:
                return []
        return []
    
    def save_todos(self):
        """Save todos to JSON file"""
        with open(self.filename, 'w') as f:
            json.dump(self.todos, f, indent=2)
    
    def add_task(self, task):
        """Add a new task"""
        todo = {
            'id': len(self.todos) + 1,
            'task': task,
            'completed': False,
            'created_at': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.todos.append(todo)
        self.save_todos()
        return todo['id']
    
    def list_tasks(self):
        """List all tasks"""
        if not self.todos:
            return None
        return self.todos
    
    def complete_task(self, task_id):
        """Mark a task as completed"""
        for todo in self.todos:
            if todo['id'] == task_id:
                todo['completed'] = True
                todo['completed_at'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                self.save_todos()
                return True
        return False
    
    def delete_task(self, task_id):
        """Delete a task"""
        initial_length = len(self.todos)
        self.todos = [todo for todo in self.todos if todo['id'] != task_id]
        if len(self.todos) < initial_length:
            self.save_todos()
            return True
        return False
    
    def clear_completed(self):
        """Clear all completed tasks"""
        initial_length = len(self.todos)
        self.todos = [todo for todo in self.todos if not todo['completed']]
        self.save_todos()
        return initial_length - len(self.todos)


def display_menu():
    """Display the main menu"""
    print("\n" + "=" * 50)
    print("         TO-DO LIST CLI APPLICATION")
    print("=" * 50)
    print("\n📋 Menu:")
    print("1. Add Task")
    print("2. View All Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Clear Completed Tasks")
    print("6. Exit")
    print("=" * 50)


def display_tasks(todos):
    """Display all tasks in a formatted way"""
    if not todos:
        print("\n📭 No tasks found! Your to-do list is empty.")
        return
    
    print("\n" + "=" * 70)
    print("YOUR TO-DO LIST:")
    print("=" * 70)
    
    pending = [t for t in todos if not t['completed']]
    completed = [t for t in todos if t['completed']]
    
    if pending:
        print("\n⏳ PENDING TASKS:")
        for todo in pending:
            print(f"  [{todo['id']}] ⬜ {todo['task']}")
            print(f"      Created: {todo['created_at']}")
    
    if completed:
        print("\n✅ COMPLETED TASKS:")
        for todo in completed:
            print(f"  [{todo['id']}] ✅ {todo['task']}")
            print(f"      Completed: {todo.get('completed_at', 'N/A')}")
    
    print("\n" + "=" * 70)
    print(f"Total: {len(todos)} | Pending: {len(pending)} | Completed: {len(completed)}")
    print("=" * 70)


def main():
    """Main function to run the to-do list CLI"""
    todo_list = TodoList()
    
    print("\n🎉 Welcome to To-Do List CLI!")
    
    while True:
        try:
            display_menu()
            choice = input("\nEnter your choice (1-6): ").strip()
            
            if choice == '1':
                # Add Task
                task = input("\n📝 Enter task description: ").strip()
                if task:
                    task_id = todo_list.add_task(task)
                    print(f"✅ Task added successfully! (ID: {task_id})")
                else:
                    print("❌ Task cannot be empty!")
            
            elif choice == '2':
                # View All Tasks
                tasks = todo_list.list_tasks()
                display_tasks(tasks)
            
            elif choice == '3':
                # Mark Task as Completed
                tasks = todo_list.list_tasks()
                if tasks:
                    display_tasks(tasks)
                    try:
                        task_id = int(input("\nEnter task ID to mark as completed: "))
                        if todo_list.complete_task(task_id):
                            print(f"✅ Task {task_id} marked as completed!")
                        else:
                            print(f"❌ Task {task_id} not found!")
                    except ValueError:
                        print("❌ Invalid task ID!")
                else:
                    print("\n📭 No tasks available!")
            
            elif choice == '4':
                # Delete Task
                tasks = todo_list.list_tasks()
                if tasks:
                    display_tasks(tasks)
                    try:
                        task_id = int(input("\nEnter task ID to delete: "))
                        if todo_list.delete_task(task_id):
                            print(f"✅ Task {task_id} deleted successfully!")
                        else:
                            print(f"❌ Task {task_id} not found!")
                    except ValueError:
                        print("❌ Invalid task ID!")
                else:
                    print("\n📭 No tasks available!")
            
            elif choice == '5':
                # Clear Completed Tasks
                count = todo_list.clear_completed()
                if count > 0:
                    print(f"✅ Cleared {count} completed task(s)!")
                else:
                    print("ℹ️  No completed tasks to clear.")
            
            elif choice == '6':
                # Exit
                print("\n👋 Thank you for using To-Do List CLI!")
                print("Goodbye!")
                break
            
            else:
                print("❌ Invalid choice! Please enter a number between 1-6.")
        
        except KeyboardInterrupt:
            print("\n\n👋 Exiting To-Do List CLI...")
            break
        except Exception as e:
            print(f"❌ An error occurred: {e}")


if __name__ == "__main__":
    main()