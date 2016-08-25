from sys import stdin
import time
start = time.clock()
storst = float('-inf')
for i in stdin:
    if int(i) > float(storst):
        storst = int(i)
end = time.clock()
print(storst, "time(s): " + str(end-start))
