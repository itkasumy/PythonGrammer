class A(object):
    pass


tmp = True
tmp = False
tmp = 0
tmp = 1
tmp = 2
tmp = 0.0
tmp = -1
tmp = ''
tmp = ' '
tmp = []
tmp = [11]
tmp = ()
tmp = (11,)
tmp = {}
tmp = {'name': 'lisi'}
tmp = A()
tmp = None

if tmp:
    print('条件满足, True')
else:
    print('条件不满足, False')
