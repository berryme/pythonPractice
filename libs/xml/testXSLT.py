import unittest

from .nilXslt import *

class MyTestCase(unittest.TestCase):
    def test_files(self):
        files = load_files('/', '*.xml')
        self.assertEqual(len(files), 3)
        for file in files:
            transform(file)


if __name__ == '__main__':
    unittest.main()
