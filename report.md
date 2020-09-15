# Report for 2020-sensor-miniproject

### Contributors: Ben Chan (BU ID: U25040522), Chasity Chavez (BU ID: U94672859)


## Task 0
##### 1) What is the greeting string issued by the server to the client upon first connecting?
The greeting string issued is "ECE Senior Capstone IoT simulator"
          
          
## Task 2
#### 1) Report median and variance observed from temperature data

Temperature | Median | Variance
------------|--------|----------
Lab1 | 20.999 | 4.696

#### 2) Report median and variance observed from the occupancy data

Occupancy | Median | Variance
----------|--------|----------
Lab1 | 5.0 | 5.432

#### 3) Plots of Probability Distribution Functions for each Sensor
![image](https://github.com/bchan/2020-sensor-miniproject/blob/main/images/pdf_co2_lab1.png?raw=true)
![image](https://github.com/bchan/2020-sensor-miniproject/blob/main/images/pdf_occupancy_lab1.png?raw=true)
![image](https://github.com/bchan/2020-sensor-miniproject/blob/main/images/pdf_temp_lab1.png?raw=true)

#### 4) What is the mean and variance of the time interval of the sensor readings? Please plot its probability distribution function. Does it mimic a well-known distribution for connection intervals in large systems? 

Time Interval Statistics
Mean | Variance
-----|----------
1.047 | 1.084


Plot: ![image](https://github.com/bchan/2020-sensor-miniproject/blob/main/images/pdf_timeinterval.png?raw=true)

We observed that it mimics the Erlang disctribution, which is a popular distribution used to predict waiting times.


## Task 3
#### 1) Implement an algorithm that detects anomalies in temperature sensor data. Print the percent of "bad" data points and determine the temperature median and variance with these bad data points discarded--the same room you did in Task 2 Question 1.

Percentage/Fraction of Bad Readings for lab1: 1.5558698727015559% (11/707)

With bad readings removed:

Median | Variance
-------|----------
20.999 | 0.268

#### 2) Does a persistent change in temperature always indicate a failed sensor?
Not necessarily, it depends on how big change is, because temperature can change slightly due to outside factors, such as doors opening or closing. Bigger, more significant changes would be better to indicate failed sensors.

#### 3) What are possible bounds on temperature for each room type?
Top bounds were found using following formula: mean + (2 * standard deviation)
Bottom bounds were found using following formula: mean - (2 * standard deviation)

###### lab1
top_bound | bottom_bound
----------|-------------
25.344 | 16.676

###### class1 
top_bound | bottom_bound
----------|-------------
37.455 | 16.723

###### office
top_bound | bottom_bound
----------|-------------
27.779 | 18.422


## Task 4
#### 1) How is this simulation reflective of the real world?
The simulation is reflective of the real world in the way that sensor data usually reflects a certain distribution in the real world. For example, the mimicking of the Erlang distribution shows that there is a correlation with the data recieved from the sensors and the data collected from other similar simulations or experiments. Because of this, if we pick from that same distribution, we should have a simulation that reflects the real world to a certain extent. Similarly, just like in the real world, some data may be considered 

#### 2) How is this simulation deficient? What factors does it fail to account for?
The simulation is deficient in the way that it does not account for all real world factors. For example, an essential real world factor that the simulation failed to account for is human interaction or modification. These may include:
          - People opening or closing doors, causing an unprecedented change in data,
          - People modifying the sensor while it is still picking up data,
          - Technical difficulties, such as a lag in data recipency,
          - And more factors.

#### 3) How is the difficulty of initially using this Python websockets library as compared to a compiled language e.g. C++ websockets
Using the Python websockets is easier as compared to a compiled language because of it’s more straightforward approach and the need for less set-up procedures. In addition, less methods need to be used or called, adding for a format which is easier to follow.

#### 4) Would it be better to have the server poll the sensors, or the sensors reach out to the server when they have data?
It would be better to have the server poll the sensor. The reason for this is that having the server poll the sensors allows for less wasted resources in the sense that the server won’t be waste time waiting for the sensors to reach out. In addition, since the sensor data is not wanted at all time, having the server poll the data allows it to recieve the data when it needs it, allowing for less idle time in while waiting.
