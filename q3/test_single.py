import unittest

from single import triple_check


class TestTripleCheck(unittest.TestCase):
	def setUp(self):
		self.tripple_list = [5, 3, 4, 3, 5, 5, 3] 
		self.non_triple = [3,3,3,2,2,2,2,1]
		self.more_single = [3,3,3,2,2,2,1,4]


	def tearDown(self):
		self.tripple_list = None

	# test a valid tripple check string
	def test_single_items(self):
		test = triple_check(self.tripple_list)
		self.assertEqual(test,4)

	# test list that contains item count not equal to 3
	def test_invalid_list_triple(self):
		test = triple_check(self.non_triple)
		self.assertEqual(test,'Invalid list')

	# test list that more than single item count
	def test_invalid_list_single(self):
		test = triple_check(self.more_single)
		self.assertEqual(test,'Invalid list')


if __name__ == '__main__':
	unittest.main()