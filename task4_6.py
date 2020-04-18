class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('{} поехала!'.format(self.name))

    def stop(self):
        print('{} остановилась!'.format(self.name))

    def turn(self, direction):
        print('{} повернула на {}!'.format(self.name, direction))

    def show_speed(self):
        print('текущая скорость:', self.speed)


class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print('Вы привысили максимально допустимую скорость!')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        print('текущая скорость:', self.speed)
        if self.speed > 40:
            print('Вы привысили максимально допустимую скорость!')


class PoliceCar(Car):
    pass


sport_car = SportCar(120, 'красная', 'спортивная машина', False)
town_car = TownCar(80, 'белая', 'городская машина', False)
work_car = WorkCar(70, 'коричневая', 'рабочая машина', False)
police_car = PoliceCar(80, 'синяя', 'полицейская машина', True)

sport_car.show_speed()
town_car.show_speed()
work_car.show_speed()
police_car.show_speed()
sport_car.turn('лево')
