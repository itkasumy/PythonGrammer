class Cat(object):

    def __init__(self):
        print('__init__', self)

    def __new__(cls, *args, **kwargs):
        obj = object.__new__(cls)
        print('__new__', obj)
        return obj


cat = Cat()
print("创建了对象 %s" % cat)
