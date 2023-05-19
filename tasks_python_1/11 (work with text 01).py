y = input()
x = y.split()
def calculate_num(x):
    c = 0
    n = x[0]
    for i in x:
        a = x.count(i)
        if a > c:
            c = a
            n = i
    return n
print(calculate_num(x))
def longest_word(x):
    return max(set(x), key = len)
print(longest_word(x))