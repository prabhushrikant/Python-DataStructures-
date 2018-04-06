#!/bin/python

import sys

# Program to find all permutations of a given string
# e.g. string is 'abc' it should produce output
# abc
# bac
# cba
# cab
# bca
# acb

def get_max_permutations(n):
    if n == 0:
        return 1
    else:
        return n * get_max_permutations(n-1)

def swap(curr_s, i, j):
    new_s = list(curr_s)
    new_s[i], new_s[j] = new_s[j], new_s[i]
    return ''.join(new_s)

# works for smaller strings but not longer
def permutations_recursive(curr_s, set_s):
    if curr_s in set_s:
        return
    else:
        print curr_s
        set_s.append(curr_s)
        i = 0
        while i < len(curr_s):
            j = 0
            while j < len(curr_s):
                if i != j:
                    new_s = swap(curr_s, i, j)
                    permutations_recursive(new_s, set_s)
                j += 1
        i += 1
        return

def permutations_recursive1(s, prefix):
    if len(s) == 0:
        print prefix
    else:
        i = 0
        while i < len(s):
            rem = s[:i]+s[i+1:]
            permutations_recursive1(rem, prefix+s[i])
            i += 1

# works for smaller strings but takes too long for longer strings, like try "shrikant"
def permutations_iterative(s_set, set_i):
    while set_i < len(s_set):
        print len(s_set),
        print set_i,
        curr_s = s_set[set_i]
        print curr_s
        i = 0
        while i < len(curr_s):
            j = 0
            while j < len(curr_s):
                if i != j:
                    new_s = swap(curr_s, i, j)
                    if new_s not in s_set:
                        s_set.append(new_s)
                j += 1
            i += 1
        set_i += 1

if __name__ == "__main__":
    s = raw_input().strip()
    s_set = []
    s_set.append(s)
    max_permutations = get_max_permutations(len(s))
    print max_permutations
    # result = permutations_iterative(s_set, 0)
    result = permutations_recursive(s, [])
    # permutations_recursive1(s,"", 0)
    # print result