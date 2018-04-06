#code
class Interval:
    def __init__(self, start_time=None, end_time=None):
        self.start= start_time
        self.end= end_time

def swap(intervals, a, b):
    intervals[a], intervals[b] = intervals[b], intervals[a]

def sortInterval(intervals):
    i = 0;
    while i < len(intervals)-1:
        j = i+1
        while j < len(intervals):
            if intervals[j].start < intervals[i].start:
                swap(intervals, j, i)
            elif intervals[j].start == intervals[i].start:
                if intervals[j].end < intervals[i].end:
                    swap(intervals, j, i)
            j += 1
        i += 1
    return intervals

def findPlatforms(sorted_intervals):
    if not sorted_intervals or len(sorted_intervals) == 0:
        return 0
    elif len(sorted_intervals) == 1:
        return 1
    else:
        platforms = 0
        i = 0
        while i < len(intervals)-1:
            if intervals[i+1].start < intervals[i].end:
                platforms += 1
            i += 1
        return platforms

if __name__ == '__main__':
    intervals_start = [940,950,900,1100,1100,1500,1800]
    intervals_end = [1200,1120,910,1130,1115,1900,2000]
    intervals = []
    print(intervals_start)
    print(intervals_end)
    i = 0
    while i < len(intervals_start):
        new_interval = Interval(intervals_start[i],intervals_end[i])
        intervals.append(new_interval)
        i += 1

    sorted_intervals = sortInterval(intervals)

    for i in sorted_intervals:
        print str(i.start) + ",",
    print
    for i in sorted_intervals:
        print str(i.end) + ",",

    print
    print "minimum platforms required :"+str(findPlatforms(sorted_intervals))