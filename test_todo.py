#!/usr/bin/env python3
"""
Test cases for To-Do List CLI Application
"""

import unittest
import sys
import os
import json

# Add parent directory to path to import todo
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from todo import TodoList


class TestTodoList(unittest.TestCase):
    """Test cases for TodoList class"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.test_file = "test_todos.json"
        self.todo_list = TodoList(self.test_file)
        # Clear any existing test data
        self.todo_list.todos = []
        self.todo_list.save_todos()
    
    def tearDown(self):
        """Clean up test files"""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
    
    def test_add_task(self):
        """Test adding a task"""
        task_id = self.todo_list.add_task("Test task 1")
        self.assertEqual(task_id, 1)
        self.assertEqual(len(self.todo_list.todos), 1)
        self.assertEqual(self.todo_list.todos[0]['task'], "Test task 1")
        self.assertFalse(self.todo_list.todos[0]['completed'])
    
    def test_add_multiple_tasks(self):
        """Test adding multiple tasks"""
        self.todo_list.add_task("Task 1")
        self.todo_list.add_task("Task 2")
        self.todo_list.add_task("Task 3")
        self.assertEqual(len(self.todo_list.todos), 3)
    
    def test_list_tasks_empty(self):
        """Test listing tasks when list is empty"""
        tasks = self.todo_list.list_tasks()
        self.assertIsNone(tasks)
    
    def test_list_tasks(self):
        """Test listing tasks"""
        self.todo_list.add_task("Task 1")
        self.todo_list.add_task("Task 2")
        tasks = self.todo_list.list_tasks()
        self.assertIsNotNone(tasks)
        self.assertEqual(len(tasks), 2)
    
    def test_complete_task(self):
        """Test completing a task"""
        task_id = self.todo_list.add_task("Complete me")
        result = self.todo_list.complete_task(task_id)
        self.assertTrue(result)
        self.assertTrue(self.todo_list.todos[0]['completed'])
        self.assertIn('completed_at', self.todo_list.todos[0])
    
    def test_complete_invalid_task(self):
        """Test completing a non-existent task"""
        result = self.todo_list.complete_task(999)
        self.assertFalse(result)
    
    def test_delete_task(self):
        """Test deleting a task"""
        task_id = self.todo_list.add_task("Delete me")
        result = self.todo_list.delete_task(task_id)
        self.assertTrue(result)
        self.assertEqual(len(self.todo_list.todos), 0)
    
    def test_delete_invalid_task(self):
        """Test deleting a non-existent task"""
        result = self.todo_list.delete_task(999)
        self.assertFalse(result)
    
    def test_clear_completed(self):
        """Test clearing completed tasks"""
        # Add some tasks
        id1 = self.todo_list.add_task("Task 1")
        id2 = self.todo_list.add_task("Task 2")
        id3 = self.todo_list.add_task("Task 3")
        
        # Complete some tasks
        self.todo_list.complete_task(id1)
        self.todo_list.complete_task(id2)
        
        # Clear completed
        count = self.todo_list.clear_completed()
        self.assertEqual(count, 2)
        self.assertEqual(len(self.todo_list.todos), 1)
    
    def test_save_and_load(self):
        """Test saving and loading todos from file"""
        self.todo_list.add_task("Persistent task")
        
        # Create new instance to test loading
        new_todo_list = TodoList(self.test_file)
        self.assertEqual(len(new_todo_list.todos), 1)
        self.assertEqual(new_todo_list.todos[0]['task'], "Persistent task")


def run_tests():
    """Run all tests and return results"""
    # Create test suite
    suite = unittest.TestLoader().loadTestsFromTestCase(TestTodoList)
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Print summary
    print("\n" + "=" * 70)
    print("TEST SUMMARY:")
    print("=" * 70)
    print(f"Tests run: {result.testsRun}")
    print(f"Successes: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    print("=" * 70)
    
    # Return exit code
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    exit_code = run_tests()
    sys.exit(exit_code)