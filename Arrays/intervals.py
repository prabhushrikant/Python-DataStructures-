#given a job start and end time and number of resources it takes
#find maximum number of resources can be taken at any point of time.
#so at any point if job is
# inputdata = [
#     Job(0,  10,  5),
#     Job(0,  2,   1),
#     Job(0,  2,   2),
#     Job(5,  20,  5),
#     Job(11, 20, 10),
# ]
# Between job intervals [5-20] and [11-20] maximum number of resources will be used , i.e. 15

from pprint import pprint

class Job:
    maxx = 0

    def __init__(self, start, end, val):
        self.start = start
        self.end = end
        self.val = val

    def __repr__(self):
        return "Job(start: {}, end: {}, resources: {})".format(self.start, self.end, self.val)

def sort_input(inputdata):
    for i in range(len(inputdata)):
        for j in range(len(inputdata)):
            if inputdata[i].start < inputdata[j].start:
                inputdata[i], inputdata[j] = inputdata[j], inputdata[i]
            elif inputdata[i].start == inputdata[j].start:
                if inputdata[i].end < inputdata[j].end:
                    inputdata[i], inputdata[j] = inputdata[j], inputdata[i]

    return inputdata

# solution iterating over job interval boundries.
# def get_max(sorteddata):
#     maxx = 0
#     min_end = 0
#     min_end_val = 0
#     curr = sorteddata[0].val
#     for i in range(len(sorteddata)-1):
#         # curr += sorteddata[i].val
#
#         if sorteddata[i+1].start > sorteddata[i].end:
#             curr -= sorteddata[i].val
#         else:
#             if min_end < sorteddata[i+1].start:
#                 curr -= min_end_val
#                 min_end = sorteddata[i].end
#                 min_end_val = sorteddata[i].val
#             curr += sorteddata[i+1].val
#
#         if min_end > sorteddata[i].end:
#             min_end = sorteddata[i].end
#             min_end_val = sorteddata[i].val
#
#         if curr > maxx:
#             maxx = curr
#
#         print i, curr, maxx
#
#     return maxx


# solution iterating over time interval boundries. (simpler) (complexity is heigher)
def get_max(sorteddata):
    min_time = sorteddata[0].start
    max_time = sorteddata[len(sorteddata)-1].end
    maxx = 0
    i = min_time
    while i <= max_time:
        curr = 0
        for job in sorteddata:
            if job.start <= i and i < job.end:
                curr += job.val
                if curr > maxx:
                    maxx = curr
            elif i == job.end:
                curr -= job.val
        i += 1
    return maxx

# if __name__=='__main__':

# sorteddata = [
#     Job(0,  2,   1),
#     Job(0,  2,   8),
#     Job(0,  10,  5),
#     Job(5,  20,  5),
#     Job(11, 20, 10),
# ]

inputdata = [
    Job(0,  10,  5),
    Job(0,  2,   1),
    # Job(0,  2,   20),
    Job(5,  20,  5),
    Job(11, 20, 10),
]


sorteddata = sort_input(inputdata)
pprint(sorteddata)
print str(get_max(sorteddata))