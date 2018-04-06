# Enter your code here. Read input from STDIN. Print output to STDOUT
lookup = {}

def get_suggestion(user_input):
    max = 0
    suggestions = []
    all_suggestions = lookup[user_input]
    if all_suggestions is not None:
        for key,value in all_suggestions.iteritems():
            if value > max:
                suggestions = [] #clear the list
                max = value
                suggestions.append(key)
            elif value == max:
                suggestions.append(key)
    return max, suggestions

def rebuild_lookup(user_input):
    s = user_input.lower()

    for key in lookup:
        if key != s:
            all_suggestions = lookup[key]
            if all_suggestions is not None:
                if s in all_suggestions:
                    all_suggestions[s] += 1
                else:
                    all_suggestions[s] = 1
            else:
                lookup[key] = {s:1}

    if s not in lookup:
        lookup[s] = None


if __name__=='__main__':
    #lookup is map of map <keyword, map<query, value>>

    # N = raw_input()
    # N = 9
    i = 0

    inputs = ["A retail",
             "A restaurant",
             "A sales",
             "B retail",
             "B sales",
             "B part_time",
             "C retail",
             "C part_time"
            ]

    # print "number of cases: " + str(N)
    # while i < int(N):
    for input in inputs:
        # input_terms = raw_input().strip().split(' ')
        input_term = input.strip().split(' ')
        user = input_term[0]
        user_input = input_term[1]

        if user_input in lookup:
            score, suggestions = get_suggestion(user_input)
            print str(score) + ",",
            print suggestions
        else:
            print 0
        rebuild_lookup(user_input)
        # i += 1