import unittest

from additive import additive_sequence


class TestAddative(unittest.TestCase):
	def setUp(self):
		self.addative = [6, 6, 12, 18, 30,48 ]
		self.not_addative = [6, 6, 12, 18, 30,8 ]
	
	def tearDown(self):
		self.addative = None
		self.not_addative = None

	# test list that is an addative
	def test_additive_list(self):
		test = additive_sequence(self.addative)
		self.assertTrue(test)

	# test list that is not an addative
	def test_non_additive_list(self):
		test = additive_sequence(self.not_addative)
		self.assertFalse(test)


if __name__ == '__main__':
	unittest.main()
