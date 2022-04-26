import unittest
import main

class Test(unittest.TestCase):

  def test_check_if_normal_year(self):
    """
      Year is normal year if it is not divisible by 4, 100 and 400
    """
    self.assertFalse(main.leap_year(2001))


if __name__ == '__main__':
  unittest.main()