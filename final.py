import time
import serial

from twilio.rest import Client
def send_msg(msg,load):
  account_sid = "AC15ad7f2417dd92290cb0cc1a2ce51f9a"
  auth_token = "c43fea34d2c70c754c326b6bbbf82a86"
  client = Client(account_sid,auth_token)
  message = client.messages.create(to="+917011792723", from_="+13163335246", body= msg + "Overloading is : " + load +"watt")
  print (message.sid)


ports = ["/dev/ttyACM0","/dev/ttyACM1","/dev/ttyACM2","/dev/ttyACM3","/dev/ttyACM4"]
for port in ports:
  try:
    ser = serial.Serial(port,9600)
    break
  except:
    pass

def Delay():
  for i in range(5):
    read_serial = ser.readline()
    load = float(read_serial)
    b = str(load)
    with open("test.txt", "a") as myfile:
      myfile.write(b + " ")
    print(load) 
  return load

ts = 2.25
while(True):  
    read_serial = ser.readline()
    load = float(read_serial)
    b = str(load)
    with open("test.txt", "a") as myfile:
      myfile.write(b + " ")
    print(load)
    if(load > ts):
      load = Delay()      
    if(load >ts):
      msg = "Please Turn off some appliances, Otherwise you will face BROWNOUT..."
      l = load-ts
      l = str(l)
      send_msg(msg,l)
      print("Please Turn off some appliances, Otherwise you will face BROWNOUT...")
      load = Delay()
    if(load > ts):
      ser.write(b'offnonE')
      load = Delay()
      ser.write(b'onnonE')
      load = Delay()
    if(load > ts):
      msg = "Please Turn off some appliances, Otherwise you will face BLACKOUT..."
      l = load-ts
      l = str(l)
      send_msg(msg,l)
      print("Please Turn off some appliances, Otherwise you will face BLACKOUT...")
      load = Delay()
    if(load > ts): 
      ser.write(b'off')
      load = Delay()
      ser.write(b'on')

