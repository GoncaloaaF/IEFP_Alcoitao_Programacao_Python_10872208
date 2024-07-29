from Contacto import *
from Agenda import *
import uuid
import  time as t

ct = Contacto("nome","email", "+351 32131233")


my_agenda = Agenda("Agenda 1")


"""

listt  - []
set  -   {}
dict -   {:}


"""


mySet: set = {"val1", "val2"}


print(mySet.__len__())

mySet.add("val3")

print(mySet.__len__())

mySet.add("val8")

print(mySet.__len__())


mySet2 = set()
print(mySet2.__len__())

st = t.time()
for i in range(0, 10000):
    mySet2.add(uuid.uuid4())

ft = t.time()


tempo = ft-st
print(f"tempo: {tempo}")
print(mySet2.__len__())

print(uuid.uuid4())

'''
uuid
tempo: 0.028271913528442383
tempo: 0.029098987579345703

int 
tempo: 0.0009739398956298828
tempo: 0.0008869171142578125



c54fd696-fe51-423e-a132-ba2dc084be03 -> 36



1
2
3


'''
k = uuid.uuid4()

st = t.time()
for elm in mySet2:
    print(elm == k)
ft = t.time()


print(f"tempo: {tempo}")


'''
tempo: 0.0009520053863525391
tempo: 0.0009300708770751953


tempo: 0.0282289981842041
tempo: 0.02832317352294922


'''



ct = Contacto("nome","email", "+351 32131233")

ct.showId()