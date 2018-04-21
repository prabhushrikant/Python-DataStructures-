from collections import deque as q

n = 5  # in mins
unit = 1  # seconds
q_size = (5 * 60) / 1
curr_count = 0
web_hit_q = q([])


# continuously tracking the count.
def collect_hits():
    curr_count += 1


# called after every unit time
def record_hits():
    if len(web_hit_q) > q_size:
        web_hit_q.popleft()
    web_hit_q.append(curr_count)
    curr_count = 0


def get_hits():
    no_of_users = 0
    for i in range(len(web_hit_q)):
        no_of_users += web_hit_q[i]

    return no_of_users
