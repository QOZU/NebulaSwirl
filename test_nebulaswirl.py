# test_nebulaswirl.py
"""
Tests for NebulaSwirl module.
"""

import unittest
from nebulaswirl import NebulaSwirl

class TestNebulaSwirl(unittest.TestCase):
    """Test cases for NebulaSwirl class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = NebulaSwirl()
        self.assertIsInstance(instance, NebulaSwirl)
        
    def test_run_method(self):
        """Test the run method."""
        instance = NebulaSwirl()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
