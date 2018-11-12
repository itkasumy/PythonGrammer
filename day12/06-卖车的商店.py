class Car(object):

    def move(self):
        print('车在跑...')


class CarStore(object):

    def order(self):
        car = Car()
        return car


carStore = CarStore()

car1 = carStore.order()
print('买到一辆新车:%s' % car1)

car2 = carStore.order()
print('买到一辆新车:%s' % car2)

