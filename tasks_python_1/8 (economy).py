s, d = input(), input()
list_s = s.split(",")
list_d = d.split(",")
ch = 0
for i in range(len(list_s)):
    for j in range(len(list_d)):
        if list_s[i] == list_d[j]:
            ch+=1
print(ch)