file = open("./a.txt", 'w')
file.write('Hello Ksm')
file.close()

fileR = open('./a.txt', 'r')
cont = fileR.read()
print(cont)
fileR.close()
