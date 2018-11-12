a = {11, 22, 33, 44, 55, 22, 66, 44}
print(type(a))

b = {11, 22, 22, 44, 44, 33, 55, 33, 11, 22}
print(b)
b.add(66)
b.remove(44)
print(b)

c = set(a)
print(c)

d = list(b)
print(d)
