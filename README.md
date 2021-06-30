# Smart-Transformer-Monitoring-Controlling-System
## Description
This project is developed by [Sooraj Mishra](https://github.com/soorajmishra10) with [Anurag Saraswat](https://github.com/saraswatanurag14) under the guidance 
of Mr. Praphull Nayak at RKGIT, Ghaziabad, India. 
We have developed a test bed for Smart Transformer Monitoring & Controlling System. The objective of this system is to monitor the power consumption 
of customers and take smart preventive actions to reduce the transformer overloading.


## Tools Used
* Programming Languages: Python
* Micro-controllers: Raspberry Pi 3, Arduino Uno
* Sensors: Current Sensor(ACS712), Voltage Sensor(25V), 1 Channel Relay Module(5V)
* APIs: Twilio API
* Others: LED Bulbs(9W)
* OS: Raspberry Pi OS

## Important terms/concepts
* It is assumed that the customers have 02 lines in their households for eletricity.
* **Essential Line:** All the essential equipments/devices of a house are connected to this line like lights, fans etc.
* **Non-essential Line:** All the luxurious(or non-essential) equipments/devices are connected to this line like Air-Conditioners, Washing Machines etc.
* **Threshold Value:** A threshold value is set by the electricity operator for local house power consumption.
* **Brownout:** Brownout is a situation when due to overloading, the electricity of the non-essential line has been stopped for some fixed time.   
* **Blackout:** Blackout is a situation when due to overloading, the electricity of the whole house(i.e. the non-essential as well as essential line) has been stopped for some fixed time.

## Work FLow
* The power consumption of each house is monitored at the powerstation in real-time.
* Whenever any house consumes the power more than the threshold value(overloading) for a fixed period of time, a Brownout warning message is sent to the registered mobile no. in real-time
and a Brownout timer starts.
* If the consumer does not reduces the load below the threshold value within the specified time, the Brownout timer expires and Brownout occurs.
* After some fixed amount of the time, the electricity will be resumed as previous.
* If the load is still more than threshold value(overloading even after Brownout), another Blackout warning message will be sent to the registered mobile no. and a Blackout timer starts.
* If the consumer does not reduces the load below threshold value within specified time, the Blackout timer expires and Blackout occurs.
* After some fixed amount of time, the electricity will be resumed as previous.
* In this way, the overloading is monitored and load curtailment is done to reduce the transformed load smartly.




