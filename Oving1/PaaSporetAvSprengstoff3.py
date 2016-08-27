from sys import stdin
from time import clock
start = clock()
var =max(int(i) for i in stdin.readlines())
end = clock()
print(var, "time(): "+str(end-start))
