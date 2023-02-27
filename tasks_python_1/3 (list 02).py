import random
list1, list2, list3 = [], [], []
long1 = random.randrange(50, 101)
for i in range(long1):
    list1.append(random.randrange(0, 10000))
long2 = random.randrange(50, 101)
for j in range(long2):
    list2.append(random.randrange(0, 10000))
for h in range(len(list1)):
    if list1[h] in list2:
        list3.append(list1[h])
print(list3)