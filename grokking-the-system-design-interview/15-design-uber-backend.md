## 1. What is Uber?

## 2. Requirements and Goals of the System

drivers, customers

drivers -> regularly notify service about cur loc and availability
passengers -> see all nearby drivers
customers can request a ride -> all nearby drivers notified
once driver & customer accept -> see each other's cur loc until trip finishes
upon reaching dest, driver marks the journey to complete -> become vailble for next ride

## 3. Capacity Estimation and Constraints
Assumption:
- 300M customers, 1M drivers 
- 1M daily active customers, 500k daily active drivers
- 1M daily rides
- Active drivers notify cur loc every 3 sec
- Customer puts request for ride -> system notifies drivers in real-time

## 4. Basic System Design and Algorithm
Yelp's QuadTree solution was not built for dynamic and frequent updates.

Issues:
- Driver's are reporing every three seconds - update QuadTree datastructure to reflect that.
- We need quick mechanism to propagate cur loc of all nearby drivers to any active customers

### DriverLocationHashTable:
Do we need to modify our QuadTree every time a driver reports their location?
Since all active drivers report their location every 3 seconds, there will be a lot more updates happening to our tree than querying for nearby drivers. 
What if we keep latest position reported by all drivers in hash table(`DriverLocationHT`) and update QuadTree less frequently?

Memory:
- DriverID (3 bytes - 1 million drivers)
- Old lat (8 bytes)
- Old lng (8 bytes)
- New Lat (8 bytes)
- New Lng (8 bytes)

Total 35 bytes

1 million drivers * 35 bytes => 35 MB

* How much bandwidth will our service consume to receive location updates from all drivers?
DriverID + location = 3 + 16 = 19 bytes

every 3 seconds from 500k daily active drivers = 9.5MB per 3 seconds

* Do we need to distribute DriverLocationHT onto multiple servers?

* How can we efficiently broadcast the driver’s location to customers? 
Push Model where server will push positions to all relevant users

## 5. Fault Tolerance and Replication
What if a Driver Location server or Notification server dies? 
- Need replicas of these servers
- We can also store this data in SSD for fast IOs

## 6. Ranking
