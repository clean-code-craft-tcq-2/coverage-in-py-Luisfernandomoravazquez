import unittest
import typewise_alert


class TypewiseTest(unittest.TestCase):
  def test_infers_breach_as_per_limits(self):
    self.assertTrue(typewise_alert.check_temperature(-3,"PASSIVE") == 'TOO_LOW')
    self.assertTrue(typewise_alert.check_temperature(10,"PASSIVE") == 'NORMAL')
    self.assertTrue(typewise_alert.check_temperature(90,"PASSIVE") == 'TOO_HIGH')

    self.assertTrue(typewise_alert.check_temperature(-3,"HI_ACTIVE") == 'TOO_LOW')
    self.assertTrue(typewise_alert.check_temperature(10,"HI_ACTIVE") == 'NORMAL')
    self.assertTrue(typewise_alert.check_temperature(90,"HI_ACTIVE") == 'TOO_HIGH')

    self.assertTrue(typewise_alert.check_temperature(-3,"MED_ACTIVE") == 'TOO_LOW')
    self.assertTrue(typewise_alert.check_temperature(10,"MED_ACTIVE") == 'NORMAL')
    self.assertTrue(typewise_alert.check_temperature(90,"MED_ACTIVE") == 'TOO_HIGH')

    self.assertTrue(typewise_alert.check_temperature(90,"SOMETHING_WEIRD") == 'INVALID_COOLING_TYPE')

  def test_methods(self):
    testCoolingType = typewise_alert.coolingType(10,30,typewise_alert.send_to_email)
    self.assertTrue(testCoolingType.Is_Lower_Limit_Breached(10) == False)
    self.assertTrue(testCoolingType.Is_Lower_Limit_Breached(9) == True)
    self.assertTrue(testCoolingType.Is_Upper_Limit_Breached(30) == False)
    self.assertTrue(testCoolingType.Is_Upper_Limit_Breached(31) == True)
    
    self.assertTrue(testCoolingType.check_and_alert(-10) == "TOO_LOW")
    self.assertTrue(testCoolingType.check_and_alert(20) == "NORMAL")
    self.assertTrue(testCoolingType.check_and_alert(200000) == "TOO_HIGH")
    
if __name__ == '__main__':
  unittest.main()
