import bisect
import time

x = list(range(10**6))
start1 = time.time()
i = x.index(991234)
a = x.index(912345)
print('index', i, time.time() - start1)

start2 = time.time()
j = bisect.bisect_left(x, 991234)
a = bisect.bisect_left(x, 912345)
print('bisect', j, time.time() - start2)
