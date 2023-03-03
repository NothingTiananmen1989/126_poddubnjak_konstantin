import random
long = random.randrange(5, 101)
list1= []
x = int(input())
for i in range(long):
    list1.append(random.randrange(0, 10000))

def magic(list1, x):
    if sum(list1) % x == 0:
        return True
    else:
        return False

print(magic(list1, x))