N = int(raw_input()) # the number of spaceships

info = []
start_times = []

# parse each entry and populate data into python lists
for _ in range(N):
    id, start, end = [ int(x) for x in raw_input().split() ]
    info.append((id, start, end))
    start_times.append(start)

start_times.sort() # sort start_times by increasing order

def get_num_buckets(info):
    '''
    Calculate the number of buckets (based on the log of the number of entries)

    '''
    num_buckets = 0
    ln = len(info)
    while ln > 0:
        ln = ln >> 1
        num_buckets += 1
    return num_buckets * 4

num_buckets = get_num_buckets(info)

def get_bucket_key(start):
    '''
    Calculate the appropriate bucket key for use based on the given start time

    '''

    bucket_size = len(start_times) / num_buckets
    for k in range(num_buckets):
        if start <= start_times[bucket_size * k]:
            return k
    return num_buckets - 1

def scorer(info):
    '''
    Runs the scoring algorithm on a list of info (read and processed from stdin)
    :param info: list of (spaceshipid, start_time, end_time):

    '''
    # initialize buckets using a dictionary
    buckets = {}
    for i in range(num_buckets):
        buckets[i] = set()

    info.sort(key=lambda x: x[2]) # sort by increasing end times

    result = []
    for e in info:
        ekey = get_bucket_key(e[1])

        # count the number of entries in buckets where bucket_key > ekey
        count = 0
        if ekey < num_buckets:
            for i in range(ekey+1, num_buckets):
                count += len(buckets[i])

        # count the number of entries in the bucket where bucket_key = ekey
        # and the start_time(entry) is greater than the current entry
        for v in buckets[ekey]:
            if v[1] > e[1]:
                count += 1

        # append to result and put the current entry into its bucket
        result.append((e[0], count))
        buckets[ekey].add(e)

    return result


# Output to stdout after sorting
result = scorer(info)
result.sort(key=lambda x: (x[1], x[0]))
for x, y in result:
    print x, y
