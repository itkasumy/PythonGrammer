class Car(object):

    def move(self):
        print('车在跑...')


class BMW(Car):
    pass


class Audi(Car):
    pass


class Benz(Car):
    pass


class SanTaNa(Car):
    pass


class CarStore(object):

    def order(self, type):
        factory = CarFactory()
        car = factory.createCar(type)
        return car


class CarFactory(object):
    # 造车的工厂
    def createCar(self, type):
        if type == '宝马':
            car = BMW()
        elif type == '奔驰':
            car = Benz()
        elif type == '奥迪':
            car = Audi()
        elif type == '桑塔纳':
            car = SanTaNa()

        return car


carStore = CarStore()

car1 = carStore.order('宝马')
print('买到一辆新车:%s' % car1)

car2 = carStore.order('奔驰')
print('买到一辆新车:%s' % car2)

car3 = carStore.order('奥迪')
print('买到一辆新车:%s' % car3)
