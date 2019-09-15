def gcd(x, y):
    # x>y
    if y == 0:
        return x
    return gcd(y, x % y)


print(gcd(100, 4))

import bisect

a = bisect.bisect_left()
