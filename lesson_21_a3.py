# Clock shows 'h' hours, 'm' minutes and 's' seconds after midnight.

# Your task is to make 'Past' function which returns time converted to milliseconds.

def past(h, m, s):
    return (h * 36 * 10 ** 5) + (m * 60 * 10 ** 3) + (s * 10 ** 3)

assert past(0,1,1) == 61000
assert past(1,1,1) == 3661000
assert past(0,0,0) == 0
assert past(1,0,1) == 3601000
assert past(1,0,0) == 3600000