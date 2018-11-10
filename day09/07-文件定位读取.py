file = open('a.txt')

print(file.tell())
file.read(2)
print(file.tell())
file.seek(0, 1)
print(file.tell())
file.close()