x, y, z, cost = int(input()), int(input()), int(input()), int(input())
def  calculate(x, y, z, cost):
    a = x+y-cost
    b = x+z-cost
    c = y+z-cost
    if a < 0:
        a = 99999
    if b < 0:
        b = 99999
    if c < 0:
        c = 99999
    if min(a, b, c) == a:
        return ('Алиса и Боб')
    if min(a, b, c) == b:
        return ('Алиса и Чарли')
    if min(a, b, c) == c:
        return ('Боб и Чарли')
print(calculate(x, y, z, cost))