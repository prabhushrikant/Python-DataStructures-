from collections import deque

class StackQ():

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def is_empty(self):
        return False if len(self.q1) > 0 else True

    def push(self, val):
        if not val:
            print "invalid value can't be pushed"

        else:
            self.q1.append(val)

    def pop(self):
        #copy all previously added elements
        while len(self.q1) > 1:
            e = self.q1.popleft()
            self.q2.append(e)

        #now return the last item on q1 (which was last pushed)
        self.q1.popleft()

        #Note - at this time q1 is empty.

        #move everything back from q2 to q1
        #or rename q2 to q1
        while len(self.q2) > 0:
            e = self.q2.popleft()
            self.q1.append(e);

    def show(self):
        if not self.is_empty():
            count = len(self.q1)
            while count > 0:
                e = self.q1.popleft()
                print e + ",",
                count -= 1
            print
        else:
            print "stack is empty"

if __name__ == "__main__":
    s = StackQ()
    T = int(raw_input().strip())
    while T > 0:
        inputs = raw_input().strip().split(' ')
        if inputs[0] == 'Push':
            s.push(inputs[1])
        elif inputs[0] == 'Pop':
            s.pop()

        T -= 1

    s.show();