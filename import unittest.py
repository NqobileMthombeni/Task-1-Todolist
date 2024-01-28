import unittest
from unittest.mock import patch, Mock
import tkinter as tk
import Todolist 

class TestToDoListApp(unittest.TestCase):

    def setUp(self):
        self.app = Todolist()  

    def test_add_item(self):

        with patch.object(self.app.entry, 'get', Mock()):
            self.app.entry.get.return_value = "Task 1"
            self.app.add_item()

            self.assertIn("Task 1", self.app.listbox.get(0, tk.END))

    def test_remove_item(self):

        with patch.object(self.app.listbox, 'delete', Mock()):
            
            self.app.listbox.curselection.return_value = (0,)
            self.app.remove_item()

            self.assertEqual(self.app.listbox.size(), 0)

if __name__ == '__main__':
    unittest.main()
