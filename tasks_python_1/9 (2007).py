x = str(input())
f = ''
def r(f):
    f += x[0].lower()
    for i in x[1:]:
        if f[-1].islower():
            f += i.upper()
            continue
        if f[-1].isupper():
            f += i.lower()
            continue
        if f[-1] == ' ':
            if f[-2].islower():
                f += i.upper()
                continue
            if f[-2].isupper():
                f += i.lower()
                continue
    return f
print(r(f))