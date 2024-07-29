from demoClass import *
import uuid
import time as t

c = demoClass(1, "Joao")
c2 = demoClass(1, "Joao")

print(c == c2)

print(c)


l = [1,2,3,4,5]

print(6 in l)

n = 4
if n in l:
    l.remove(n)

print(l)


mySet = set()
for i in range(0, 10000):
    mySet.add(uuid.uuid4())


id = uuid.uuid4()

st = t.time()

f = False
for i in mySet:
    if i == id:
        f = True

print(f)


ft = t.time()
print(ft-st)


'''

0.000013113021850585938
0.000012159347534179688


0.0024340152740478516
0.0015439987182617188
'''