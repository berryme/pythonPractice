import unittest

from django_apps.web.packages.xml import main


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(main.Run(), 'Yo')

    def test_main(self):
        NAME = 'yo'
        test = main.BerryClass(NAME)
        self.assertEqual(NAME, test.getName())

        self.assertEqual(5, len(test.getObjects()))

        objs = test.getObjects()

        self.assertIn("for", objs)

        self.assertNotIn("forr", objs)


if __name__ == '__main__':
    unittest.main()
