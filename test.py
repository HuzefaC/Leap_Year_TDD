import unittest
import main

class Test(unittest.TestCase):

  def test_check_if_normal_year(self):
    """
      Year is normal year if it is not divisible by 4, 100 and 400
    """
    self.assertFalse(main.leap_year(2001))
  
  def test_check_if_leap_year_only_divisible_by_4(self):
    self.assertTrue(main.leap_year(1996))

  def test_check_if_normal_year_divisible_by_4_and_100(self):
    self.assertFalse(main.leap_year(1900))


if __name__ == '__main__':
  unittest.main()