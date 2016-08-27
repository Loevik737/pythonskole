from random import randint
from sys import stdout
for i in range(0,1000000):
    stdout.write(str(randint(0,1000000))+'\n')