def check_alive(health):
    return True if health > 0 else False

assert check_alive(-2) == False
assert check_alive(0) == False
assert check_alive(1) == True
assert check_alive(3) == True