# 1. What is an online movie ticket booking system?
Purchase theatre seats online. Browse through movies currently being played to book seats anywhere anytime.

# 2. Requirements and Goals of the System
Functional Requirements:
- list different cities where its affiliate cinemas are located
- user selects city -> display movies released in that city
- user selects movie -> display cinemas running that movie and available show times
- user can choose a show at a particular cinema and book ticket
- service should be able to show user the seating arrangement
- user should be able to select multiple seats according to their preference
- user should be able to distinguish avail seats from booked ones
- user should be able to put hold on seats for five minutes before they make payment to finalize the booking
- user should be able to wait if there is chance that the seats might become available
- waiting customers should be serviced in fair, first come, first serve manner

Non-Functional Requirements:
- highly concurrent - multiple booking requests for same seats at same time. need to handle this gracefully.
- secure and database ACID compliant -> ticket booking (financial transactions)

# 3. Some design considerations
- For simplicity -> no user authentication
- No partial ticket orders
- Fairness is mandatory
- Prevent abuse -> restrict users from booking more than 10 seats at a time
- assume traffic would spike on popular/much-awaited movie releases and seats would fill up pretty fast. System should be scalable and highly available to keep up with surge and traffic.

# 4. Capacity Estimation
Traffic estimates:  
- 3 billion page views / month
- sell 10 million tickets a month

Storage estimates:
500 cities * 10 cinemas * 2000 seats * 2 shows * (50+50) bytes = 2GB / day

To store 5 years of this data, we would need around 3.6 TB.

# 5. System APIs
SearchMovies
params:
- api_dev_key
- keyword
- city
- lat_lng
- radius
- start_datetime
- end_datetime
- postal_code
- includeSpellcheck - Enum("yes", "no")
- results_per_page
- sorting_order

ReserveSeats
params:
- api_dev_key
- session_id
- movie_id
- show_id
- seats_to_reserve

# 6. DB design
City -> hasMany -> Cinemas
Cinema -> hasMany -> Halls
Movie -> hasMany -> Shows 
Show -> hasMany -> Bookings
User -> hasMany -> Bookings

# 7. High Level Design

Clients <--> LoadBalancers <--> WebServers <--> AppServers(Ticket Managements) 

-> Cache Servers
-> Databases -^

# 8. Detailed Component Design

# 9. Concurrency
Transation Isolation Levels
```
SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;

BEGIN TRANSACTION;

    -- Suppose we intend to reserve three seats (IDs: 54, 55, 56) for ShowID=99 
    Select * From Show_Seat where ShowID=99 && ShowSeatID in (54, 55, 56) && Status=0 -- free 

    -- if the number of rows returned by the above statement is three, we can update to 
    -- return success otherwise return failure to the user.
    update Show_Seat ...
    update Booking ...

COMMIT TRANSACTION;
```

# 10. Fault Tolerance

# 11. Data Partitioning
