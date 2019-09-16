# 1. What is Facebook’s newsfeed?
Constantly updating list of stories in the middle of facebook's home page.

# 2. Requirements and Goals of the System
Functional requirements:
1. Generated from posts of people, pages, groups
2. User may have many friends & follow large # of pages/groups
3. Feeds may contain img, vid, or just txt
4. Our service should support appending new posts as they arrive to the newsfeed for all active users

Non-functional requirements:
1. Our system should be able to generate any user's newsfeed in real-time - maximum latency seen by the end user would be 2s.
2. A post shouldn't take more than 5s to make it to a user’s feed assuming a new newsfeed request comes in.

# 3. Capacity Estimation and Constraints

