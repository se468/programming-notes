## 1. What is Twitter?

## 2. Requirements and Goals of the System
- Functional Requirements
- Non-functional Requirements
- Extended Requirements

## 3. Capacity Estimation and Constraints
200M DAU
100M new tweets
user follows 200 people on avg

* favorites per day: 200M users * 5 fav => 1B
* tweet views per day: 
assuming user visits timeline twice a day and visit 5 times other's pages:
200M dau * (2 * 5) * 20tweets => 28B / day

* storage estimates
100M * (280 + 30) bytes => 30GB/day
(100M/5 photos * 200KB) + (100M/10 videos * 2MB) ~= 24TB/day

* bandwidth estimates:
(28B * 280 bytes) / 86400s of text => 93MB/s 
+ (28B/5 * 200KB ) / 86400s of photos => 13GB/S 
+ (28B/10/3 * 2MB ) / 86400s of Videos => 22GB/s
Total ~= 35GB/s

## 4. System APIs
`tweet(api_dev_key, tweet_data, tweet_location, user_location, media_ids, maximum_results_to_return)`

## 5. High Level System Design

## 6. Database Schema

## 7. Data Sharding
Sharding based on UserID

Sharding based on TweetID

## 8. Cache

## 9. Timeline Generation

## 10. Replication and Fault Tolerance

## 11. Load Balancing

## 12. Monitoring

## 13. Extended Requirements

