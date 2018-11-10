class Home:
    def __init__(self, area):
        self.area = area
        self.items = []

    def __str__(self):
        allNames = []
        for item in self.items:
            allNames.append(item.name)

        return '房子的剩余空间大小是: %d 平米,存放的家具有: %s' % (self.area, allNames)

    def addItem(self, item):
        if self.area >= item.area:
            self.items.append(item)
            self.area -= item.area
        else:
            print('空间不足，无法放入新的家具')


class Bed:
    def __init__(self, area, name):
        self.area = area
        self.name = name

    def __str__(self):
        return '%s 的大小是: %d 平米' % (self.name, self.area)


home = Home(300)
print(home)

xms = Bed(5, '席梦思')
print(xms)

home.addItem(xms)
print(home)

tdc = Bed(600, 'tdc')
print(tdc)

home.addItem(tdc)
print(home)
