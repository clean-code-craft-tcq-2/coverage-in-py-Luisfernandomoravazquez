def send_to_controller(breachType):
  header = 0xfeed
  print(f'{header}, {breachType}')


def send_to_email(breachType):
  recepient = "a.b@c.com"
  if breachType == 'TOO_LOW':
    print(f'To: {recepient}')
    print('Hi, the temperature is too low')
  elif breachType == 'TOO_HIGH':
    print(f'To: {recepient}')
    print('Hi, the temperature is too high')

class coolingType:
  def __init__(self,lowerLimit, upperLimit, alerterMethod):
    self.lowerLimit = lowerLimit
    self.upperLimit = upperLimit
    self.alerterMethod = alerterMethod
  
  def check_and_alert(self, value):
    if( self.Is_Lower_Limit_Breached(value) ):
      self.alerterMethod("TOO_LOW")
      return("TOO_LOW")
    elif( self.Is_Upper_Limit_Breached(value) ):
      self.alerterMethod("TOO_HIGH")
      return("TOO_HIGH")
    else:
      return("NORMAL")

  def Is_Lower_Limit_Breached(self,value):
    return value < self.lowerLimit
  def Is_Upper_Limit_Breached(self,value):
    return value > self.upperLimit

coolingTypes_dict = {
  "PASSIVE" : coolingType(lowerLimit=0,upperLimit=35,alerterMethod=send_to_email),
  "HI_ACTIVE" : coolingType(lowerLimit=0,upperLimit=45,alerterMethod=send_to_controller),
  "MED_ACTIVE" : coolingType(lowerLimit=0,upperLimit=40,alerterMethod=send_to_email),
}
def check_temperature(value, coolingType):
  if(coolingType in coolingTypes_dict):
    coolingAnalyzer = coolingTypes_dict[coolingType]
    return coolingAnalyzer.check_and_alert(value)
  else:
    return "INVALID_COOLING_TYPE"