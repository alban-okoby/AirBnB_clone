#!/usr/bin/python3
"""A HBnB console"""

import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand

class TestConsole(unittest.TestCase):
    def setUp(self):
        self.console = HBNBCommand()

    def tearDown(self):
        pass  # Clean up, if needed

    def test_quit_command(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            with self.subTest():
                self.assertFalse(self.console.onecmd("quit"))
                self.assertEqual(mock_stdout.getvalue().strip(), "")
            with self.subTest():
                self.assertFalse(self.console.onecmd("q"))
                self.assertEqual(mock_stdout.getvalue().strip(), "")

    def test_create_command(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            with self.subTest():
                self.assertFalse(self.console.onecmd("create BaseModel"))
                self.assertTrue(mock_stdout.getvalue().strip())

    def test_show_command(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            with self.subTest():
                self.assertFalse(self.console.onecmd("create BaseModel"))
                self.assertTrue(mock_stdout.getvalue().strip())

                self.assertFalse(self.console.onecmd("show BaseModel " + mock_stdout.getvalue().strip()))
                self.assertTrue(mock_stdout.getvalue().strip())

    def test_destroy_command(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            with self.subTest():
                self.assertFalse(self.console.onecmd("create BaseModel"))
                self.assertTrue(mock_stdout.getvalue().strip())

                self.assertFalse(self.console.onecmd("destroy BaseModel " + mock_stdout.getvalue().strip()))
                self.assertEqual(mock_stdout.getvalue().strip(), "")
