#functions
import random

list = random.sample(range(100), 10)
print(list)
print(min(list))

def max_min():
    list = random.sample(range(100), 10)
    print(list)
    print(min(list))
    
max_min()

def getValues():
    list = random.sample(range(5, 10), 5)
    print(list)
    list.append(17)
    list_a = list[-1]
    print(list_a)
    print(list[:2])
    print(list[3:])
    
getValues()