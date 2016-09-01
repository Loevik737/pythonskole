from sys import stdin
from time import clock
start = clock()
var = list(int(i) for i in stdin.readlines())
var.sort()
end = clock()
print(var[len(var)-1], "time(): "+str(end-start))
