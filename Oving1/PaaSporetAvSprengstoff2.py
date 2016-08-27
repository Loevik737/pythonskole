from sys import stdin
from time import clock
start = clock()
storst = float('-inf')
for i in stdin:
    if int(i) > float(storst):
        storst = int(i)
end = clock()
print(storst, "time(s): " + str(end-start))
