class Interval:
    def __init__(self, s, e):
        self.start_time = s
        self.end_time = e


    def comparator(a, b):
        """
        Comparator to sort intervals in ascending order.
        :param a: first interval
        :param b: second interval
        :return:
        """
        if a.start_time < b.start_time:
            return -1
        elif a.start_time > b.start_time:
            return 1
        else:
            #when start times match, match the end points
            if a.end_time < b.end_time:
                return -1
            elif a.end_time > b.end_time:
                return 1
            else:
                return 0

    def __repr__(self):
        return '(%s, %s)' % (self.start_time, self.end_time)
        # return "("+str(self.start_time)+","+str(self.end_time)+")"


#driver program

inputs = [(1, 5), (1, 4), (9, 12), (3, 5), (2, 8)]

intervals = []
for input in inputs:
    interval = Interval(input[0],input[1])
    intervals.append(interval)

print repr(intervals)
#sort the intervals:

#by default are sorted in ascending order
sorted_intervals = sorted(intervals, cmp=Interval.comparator)
print repr(sorted_intervals)
sorted_intervals = sorted(intervals, cmp=Interval.comparator, reverse=True)
print repr(sorted_intervals)
