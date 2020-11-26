from functools import reduce

def next_id(arr):
    return reduce(lambda acc, x: acc + 1 if x == acc else acc, sorted(arr), 0)

assert next_id([0,1,2,3,4,5,6,7,8,9,10]) == 11
assert next_id([5,4,3,2,1]) == 0
assert next_id([0,1,2,3,5]) == 4
assert next_id([0,0,0,0,0,0]) == 1
assert next_id([]) == 0
