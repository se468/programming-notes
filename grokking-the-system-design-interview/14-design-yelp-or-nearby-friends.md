## 1. Why Yelp or Proximity Server?
- Discover nearby attractions

## 2. Requirements and Goals of the System
Functional Requirements:
- Users should be able to add/delete/update places
- Given loc(long/lat), find all nearby place with given radius
- Users should be able to add feedback/review about a place. Feedback consists of pictures, text, rating.

Non-Functional Requirements:
- real-time experience with minimum latency
- support heavy search load

## 3. Scale Estimation
Assumption:
- 500M places
- 100K queries per second (QPS)
- 20% growth in number of places and QPS each year

## 4. Database Schema
Place:
- id (8 bytes)
- Name(256 bytes)
- Latitude (8 bytes)
- Longitude (8 bytes)
- Description (512 bytes)
- Category (1 byte)

Total Size: 793 bytes

Reviews:
- id (4 bytes) - assuming each place will not have more than 2^32 reviews
- LocationID (8 bytes)
- ReviewText (512 bytes)
- Rating (1 byte)

## 5. System APIs
`search`
parameters:
- api_dev_key
- search_terms
- user_location
- radius_filter
- maximum_results_to_return
- category_filter
- sort
- page_token

returns: JSON

## 6. Basic System Design and Algorithm
a) SQL solution
- Problems with query:
`Select * from Places where Latitude between X-D and X+D and Longitude between Y-D and Y+D`

We have to search 500M indexes all the time

b) Grids
- Divide the whole map into smaller grids

`Select * from Places where Latitude between X-D and X+D and Longitude between Y-D and Y+D and GridID in (GridID, GridID1, GridID2, ..., GridID8)`

- Still problem with dense areas with a lot of places

c) Dynamic grid sizes
- Whenever grid reaches limit of 500 places, we break into 4 grids of equal size and distribute places among them
- Dense areas such as downtown Toronto will have a lot of grids
- Places like Pacific Ocean with large grids with only around coastal lines
- **Quad Tree** - Start with one node that will represent whole world in one grid

## 7. Data Partitioning
a) Sharding based on regions
- Issues:
    - What if region becomes hot?
    - Over time, some regions can end up storing a lot of places compared to others
b) Sharding based on LocationID
- Hash function will map each LocationID to a server
- To find places near a location, we have to query all servers and each server will return a set of nearby places
- A centralized server will aggregate these results to return them to user

* Will we have different QuadTree structure on different partitions? Yes, this can happen since it is not guaranteed that we will have an equal number of places in any given grid on all partitions. However, we do make sure that all servers have approximately an equal number of Places. This different tree structure on different servers will not cause any issue though, as we will be searching all the neighboring grids within the given radius on all partitions.

## 8. Replication and Fault Tolerance
Having replicas of QuadTree servers can provide alternate to data partitioning. 

To distribute read traffic, we can have replicas of each QuadTree server. 

We can have a master-slave configuration where replicas (slaves) will only serve read traffic; all write traffic will first go to the master and then applied to slaves. Slaves might not have some recently inserted places (a few milliseconds delay will be there), but this could be acceptable.

## 9. Cache
We can introduce cache in front of our database
- Memcache
- LRU

## 10. Load Balancing (LB)
1) Between clients and application servers
2) Between application servers and backend server

## 11. Ranking
Store stars in database as well as quad tree. 
- Ask each partition of QuadTree to return top 100 places with maximum popularity. 

- We didn't build our system to update place's data frequency. 
- Assuming the popularity of a place is not expected to reflect in the system within a few hours, we can decide to update it once or twice a day, especially when the load on the system is minimum.