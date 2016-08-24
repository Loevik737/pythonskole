from sys import stdin
storst = int(stdin.readline())
for i in stdin:
    if int(i) > storst:
        storst = int(i)
print(storst)