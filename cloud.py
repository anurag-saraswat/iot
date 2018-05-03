import os
import time
i = 0
while True:
  j = str(i)
  os.system("scp -i IOT_RASP.pem test.txt ubuntu@ec2-34-201-62-36.compute-1.amazonaws.com:./" +  j )
  time.sleep(30)
  i += 1
 
