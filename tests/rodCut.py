from sys import stdin
A = []
for tall in stdin:
    A.append(int(tall))


def cut_rod(p, n):
    r = [0] * (n+1)
    for i in range(1,n+1):
      q = float("-inf")
      for j in range(1,i+1):
        q = max(q,p[j] + r[i - j])
      r[i] = q
    return r[n]


print(cut_rod(A,3))

