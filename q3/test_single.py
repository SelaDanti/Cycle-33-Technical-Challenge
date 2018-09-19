import unittest

from single import single_element


class TestSingleElement(unittest.TestCase):
	def setUp(self):
		self.list_items = [5, 3, 4, 3, 5, 5, 3] 

	def tearDown(self):
		self.list_items = None

	def test_single_items(self):
		test = single_element(self.list_items)
		self.assertEqual(test,4)


if __name__ == '__main__':
	unittest.main()