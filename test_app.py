import unittest
from app import hello_world

class Testapp(unittest.TestCase):
    def test_hello_world(self):
        self.assertEqual(hello_world(), "hello, world")

if __name__ == "__main__":
    unittest.main()