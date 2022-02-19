import unittest
import typewise_alert


class TypewiseTest(unittest.TestCase):
  def test_infers_breach_as_per_limits(self):
    self.assertTrue(typewise_alert.inputFunction(-3,"PASSIVE") == 'TOO_LOW')
    self.assertTrue(typewise_alert.inputFunction(10,"PASSIVE") == 'NORMAL')
    self.assertTrue(typewise_alert.inputFunction(90,"PASSIVE") == 'TOO_HIGH')

if __name__ == '__main__':
  unittest.main()
