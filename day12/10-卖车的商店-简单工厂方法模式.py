class Car(object):

    def move(self):
        print('车在跑...')


class BMW(Car):
    pass


class BMW2016(Car):
    pass


class BMW2017(Car):
    pass


class Benz(Car):
    pass


class Benz2016(Car):
    pass


class Benz2017(Car):
    pass


class CarStore(object):

    def order(self, type):
        car = self.getCar(type)
        car.color = 'red'
        return car

    def getCar(self, type):
        pass


class BMWStore(CarStore):
    def getCar(self, type):
        factory = BMWFactory()
        car = factory.createCar(type)
        return car


class BenzStore(CarStore):
    def getCar(self, type):
        factory = BenzFactory()
        car = factory.createCar(type)
        return car


class CarFactory(object):
    # 造车的工厂
    pass


class BMWFactory(CarFactory):
    def createCar(self, type):
        if type == '宝马2016':
            car = BMW2016()
        elif type == '宝马2017':
            car = BMW2017()

        return car


class BenzFactory(CarFactory):
    def createCar(self, type):
        if type == '奔驰2016':
            car = Benz2016()
        elif type == '奔驰2017':
            car = Benz2017()

        return car


carStore = BMWStore()

car1 = carStore.order('宝马2016')
print(car1)

carStore = BenzStore()

car2 = carStore.order('奔驰2016')
print(car2)
