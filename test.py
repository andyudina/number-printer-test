import unittest

from print_numbers import get_hundred_numbers, \
                          _get_number_representation, \
                          _is_multiple_of


EXPECTED_SEQUENCE_LENGTH = 100
SEQUENCE_HEAD            = [1, 2, "Three", 4, "Five", "Three", 7, 8, "Three", "Five", 11, "Three", 13, 14, "ThreeFive"]
SEQUENCE_HEAD_LENGTH     = 15


class TestGetMultipleOf(unittest.TestCase):

    def test_multiple_of_zero(self):
        self.assertFalse(_is_multiple_of(2, 0))

    def test_multiple_of_one(self):
        self.assertTrue(_is_multiple_of(2, 1))

    def test_is_multiple(self):
        self.assertTrue(_is_multiple_of(4, 2))

    def test_is_not_multiple(self):
        self.assertFalse(_is_multiple_of(4, 3))


class TestGetNumberRespresentation(unittest.TestCase):

   def test_multiple_of_3_repr(self):
       self.assertEqual(_get_number_representation(3), "Three")

   def test_multiple_of_5_repr(self):
       self.assertEqual(_get_number_representation(5), "Five")

   def test_multiple_of_15_repr(self):
       self.assertEqual(_get_number_representation(15), "ThreeFive")

   def test_not_multiple_number_repr(self):
       self.assertEqual(_get_number_representation(1), "")


class TestGetHundredNumbers(unittest.TestCase):
    
    def test_sequence_length_is_100(self):
        sequence = list(get_hundred_numbers())
        self.assertEqual(len(sequence), EXPECTED_SEQUENCE_LENGTH)
  
    def test_first_15_numbers(self):
        ''' Tests output against predefined values.
            15 elements are enough to test all cases.
            Though it is not guaranteed that other 85  values are true, 
            it's enough compromise between test complexity and coverage.
        '''
        sequence = list(get_hundred_numbers())
        self.assertListEqual(sequence[: SEQUENCE_HEAD_LENGTH], SEQUENCE_HEAD)


if __name__ == '__main__':
    unittest.main()   
