class Time:
        '''Class to represent time of day'''

def make_time (hrs, mins, secs = 0):
    t = Time()
    t.hrs = hrs
    t.mins = mins
    t.sexs = secs
    return t

def add_times (t1,t2):
    sum_t = Time()
    sum_t.hrs +t2.hrs
    sum_t.mins = t1.secs + t2.secs
    return sum_t


