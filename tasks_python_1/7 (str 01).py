def f(x, y, z, cost):
    xy = x+y
    xz = x+z
    yz = y+z
    if xy>=cost:
        a = xy-cost
    if xz>=cost:
        b = xz-cost
    if yz>=cost:
        c = yz-cost
    list1 = [a, b, c]
    return min(list1)

x, y, z, cost = int(input()), int(input()), int(input()), int(input())

print(f(x, y, z, cost))