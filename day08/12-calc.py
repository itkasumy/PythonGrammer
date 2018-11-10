def calc(a, b, cmp):
    return cmp(a, b)


add = lambda x, y: x + y
sub = lambda x, y: x - y
mul = lambda x, y: x * y
div = lambda x, y: x / y

print(calc(6, 4, add))
print(calc(6, 4, sub))
print(calc(6, 4, mul))
print(calc(6, 4, div))
