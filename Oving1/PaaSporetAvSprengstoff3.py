from sys import stdin
import time
start = time.clock()
data = [int(i) for i in stdin.readlines()]
end = time.clock()
print(max(data),"time(s): "+str(end-start))
