file = open('a.txt', 'a')

file.write('\n1234567890')
print(file.tell())
file.seek(0, 0)
print(file.tell())
file.write('aabbcc')

file.close()

