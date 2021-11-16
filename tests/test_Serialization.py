import unittest

from flask import jsonify


class MyTestCase(unittest.TestCase):
    def test_something(self):
        message = jsonify(pv=5)
        print(message)


if __name__ == '__main__':
    unittest.main()
