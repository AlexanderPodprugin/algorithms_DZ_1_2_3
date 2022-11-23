class Hero():


    def __init__(self, name, health, armor, power, weapon):
        self.name = name 
        self.health = health 
        self.armor = armor
        self.power = power
        self.weapon = weapon 


    def print_info(self):
        print('Поприветствуйте героя -> ', self.name)
        print('Уровень здоровья ', self.health)
        print('Уровеь защиты героя ', self.armor)
        print('Сила удара ', self.power)
        print('Класс Оружия ', self.weapon) 

    def strike(self, enemy):
        print(
            ' -> УДАР ' + self.name + ' атакует ' + enemy.name +
            ' с силой ' + str(self.power) + ' используя ' + self.weapon + '\n')
        enemy.armor -= self.power
        if enemy.armor < 0:
            enemy.health += enemy.armor
            enemy.armor = 0
        #print(
            enemy.name + ' покачнулся(-ась).\nКласс брони упало до '
            + str(enemy.armor) + ' , а уровень здоровья до '
            + str(enemy.health) + '\n'

knight = Hero(' Алекс ', 60, 35, 10, ' булава ')
knight.print_info()
enemyknight = Hero(' Баграт ', 50, 30, 10, 'меч ')
enemyknight.strike(knight)









class animal():
    def init(self,type,voice):
        self.type = type
        self.voice = voice
    def make_voice(self):
        print(self.voice)
        dog = animal('Собака', 'Гав-Гав')
        dog.make_voice 
        #print(dog.type)


class Work():
    def __init__(self, place):
        self.place = place 


    def workinfo(self):
        print("Место работы: ", self.place)


class WorkingStudent(Work):



    def __init__(self, place, name, study):
        super().__init__(place)
        self.name = name
        self.study = study


    def printinfo(self):
        print("Имя: ", self.name)
        print("Место учебы: ", self.study)
        self.workinfo()

Daniil = WorkingStudent("5терочка", "Даня", "Сириус")
Daniil.printinfo()





