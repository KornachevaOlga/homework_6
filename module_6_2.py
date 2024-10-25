class Vehicle:
    __COLOR_VARIANTS = ["белый", "красный", "черный"]


    def __init__(self, owner, model, engine_power, color):


        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color


    def get_model(self):
        return f'Модель: {self.__model}'

    def get_horsepower(self):
        return f'Мощность двигателя: {self.__engine_power}'

    def get_color(self):
        return f'Цвет: {self.__color}'

    def set_color(self, new_color):
        if new_color.lower() in self.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print(f"Нельзя сменить цвет на {new_color}")

    def print_info(self):
        print(
            self.get_model(),
            self.get_horsepower(),
            self.get_color(),
            sep='\n'
        )
        print(f'Владелец: {self.owner}')



class Sedan(Vehicle):
    __PASSEGERS_LIMIT = 5

vehicle1 = Sedan('Olga', 'Sedan', '500', 'черный')
vehicle1.print_info()
vehicle1.set_color('Pink')
vehicle1.set_color('белый')
vehicle1.owner = 'Vasyok'
vehicle1.print_info()



