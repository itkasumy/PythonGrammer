class Cat:

    def __init__(self, newName):
        print('init')
        self.name = newName

    def __str__(self):
        # return 'hello'
        return '我是: %s' % self.name


mimi = Cat('咪咪')
print(mimi)
