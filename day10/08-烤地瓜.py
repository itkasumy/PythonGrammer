class Pachyrhizus:

    def __init__(self):
        self.cookedLevel = 0
        self.cookedString = '生的'
        self.condiments = []

    def __str__(self):
        return '这个地瓜是: %s,使用的调料有: %s' % (self.cookedString, self.condiments)

    def cook(self, cookedTiem):
        self.cookedLevel += cookedTiem
        print('新的程度为: %d' % self.cookedLevel)

        if self.cookedLevel <= 3:
            self.cookedString = '生的'
        elif self.cookedLevel <= 5:
            self.cookedString = '半生不熟'
        elif self.cookedLevel <= 8:
            self.cookedString = '熟的'
        else:
            self.cookedString = '烤糊了'

    def addCondiments(self, condiment):
        self.condiments.append(condiment)
        print('加入调料: %s' % condiment)


digua = Pachyrhizus()
print(digua)

digua.cook(2)
print(digua)

digua.cook(2)
print(digua)

digua.cook(2)
print(digua)

digua.cook(2)
print(digua)

digua.cook(2)
print(digua)

digua.addCondiments('孜然')
print(digua)

digua.addCondiments('蒜蓉')
print(digua)

digua.addCondiments('辣椒')
print(digua)
