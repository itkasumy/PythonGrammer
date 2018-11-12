class Cat(object):

    def __init__(self, name):
        self.name = name
        print('__init__', self)

    def __new__(cls, *args, **kwargs):
        obj = object.__new__(cls)
        print('__new__', obj)
        print(args)
        return obj


cat = Cat('小白')
print("创建了对象 %s" % cat)
