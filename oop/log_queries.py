'''

Entry in the log file is like this:
User 1 visited Page 4
User 3 visited Page 2
User 7 visited Page 9
.
.
.
Design an efficient data structure which supports queries like the following:
1) Which page[es] was visited by exactly 2 users in [a] day?
2) Which page[es] was visited by only one user exactly 2 times in a day?
3) Which page[es] was visited by ‘User 3? more than 5 times in a day?

------------

for 1:
    - dict: # unique users -> [page/day]

for 2:
    - dict: (# unique users, # visits) -> [page/day]

for 3:
    - dict: user# -> max_heap(page/day, key=#visits-by-user)

'''

==============================================

'''

Given N scientists and K black holes, each scientist can query on radius, size and temperature of a black hole, what data structure would you use?

Following queries are important:
    - Which scientist had queried on which black hole.
    - What were the queries made by that scientist.


'''

