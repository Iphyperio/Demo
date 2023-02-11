# class Poet:
#     poems = []
#     name = ''
#     date_of_death = 0
#
#     def __init__(self,name,date_of_death,poems): #конструктор объекта класса
#         self.poems = poems
#         self.name = name
#         self.date_of_death = date_of_death
#         print('Создан объект класса Poet, С именем ',self.name)
#
#     def read_poem(self):
#         print(self.poems)
#
#     def since_death(self):
#         return f'{2023-self.date_of_death} лет прошло с момента смерти'
#
# alexander = Poet('Александр',1865,['Какие-то стихи'])
# sergey = Poet('Сергей',1,'строка')
# print(alexander.name)

# alexander.name = 'Иван'
# alexander.poems = 'Шаганэ, ты моя, Шаганэ'
# print(alexander.name)
# alexander.read_poem()
# print(alexander.since_death())
#
# sergey = Poet()
# print(sergey.name)
# print(alexander.name)

# Хранятся много объектов класса User, добавленные в список:
# class User:
#     type ='Пользователь со списком попкупок'
#     class_id = 0
#     name = None
#     order = {}
#
#     def __init__(self, user_name):
#         User.class_id += 1
#         self.id = User.class_id
#         self.name = user_name
#
#     def add_purchase(self,item,price):
#         self.order.update({item:price})
#
# x = 10

#
# Sergey.order = {'Рыба':100,'Яблоко':10}
# Sergey.add_purchase('Банан',900)
# print('Сергей АйДи: ',Sergey.id)
#
# Svetlana = User('Svetlana Ivanova')
# print('Светлана АйДи: ',Svetlana.id)
#
# l = ['Банан','яблоко','капуста']
# print(l[-1])
# objects = []
# for i in range(1,21):
#     objects.append(User(f'Имя №{i}'))
#     print(objects[-1].name,objects[-1].id)
#
# objects.append(Sergey)
# objects.append(Svetlana)

# class Rectangle:
#     """Это класс, представляющий прямогуольники"""
#     def __init__(self,w = 5, h = 10):
#         self.width = w
#         self.height = h
#     def area(self):
#         return self.width * self.height
#
#     def __str__(self):
#         return f'Прямоугольник с площадью {self.area()}'
#
#
# red = Rectangle()
# blue = Rectangle(1,2)
# print(red.__dict__)
# print(red.width)
# print(Rectangle.__dict__)


# class Person:
#     message = f'Имя: , возраст: '
#
#     __private_year = 2023
#     def __init__(self,name,year_of_birth):
#         self.__name = name
#         self.__age = Person.__private_year - year_of_birth
#     def __private_say_it(self):
#         print('Никто не знал, а я бэтмен!')
#
#     def set_age(self):
#         while True:
#             age = int(input('Введите возраст: '))
#             if 18<= age <=100:
#                 self.__age = age
#                 break
#     def set_name(self):
#         while True:
#             name = (input('Введите Имя: '))
#             if 2<= len(name) <= 30:
#                 self.__name = name
#                 break
#
#     @property
#     def age(self):
#         return self.__age
#
#     def get_name(self):
#         return self.__name
#
#     def display_info(self):
#         print(f'Имя: {self.get_name()}, возраст: {self.age}')
#         self.__private_say_it()
#
#
#     @property
#     def Person_say_hello(self):
#         return f'Hello from {self.get_name()}'
#
#     @property
#     def name_and_age(self):
#         return [self.get_name(),self.age]
#
#
# tom = Person('Том',1980)
#
# print(tom.Person_say_hello)
# print(tom.message)
#
# print(tom.name_and_age[1])

# class Wood:
#     pass
#
# class Artist:
#     painting = 'Картина'
#     def Paint(self):
#         print('Пишет картину')
#
# class Poet:
#     poem = 'Стих'
#     def Write(self):
#         print('Пишет стих')
#
# class MultiArtist(Artist,Poet):
#
#     def EverythingAtOnce(self):
#         print('Наш мульти-артист: ',super().poem,super().painting)
#         super().Write()
#         super().Paint()
#
# super_artist = MultiArtist()
# super_artist.EverythingAtOnce()
#
# l = MultiArtist.mro()
# for c in l:
#     print(c.__name__,end=' -->')

#
# class Person:
#     name = 'Карл'
#     @property
#     def Tell_my_name(self):
#         #каки-ето дополнительные функции могут быть тут
#         return Person.name
#
#     @staticmethod
#     def is_adult(age):
#         if age >= 18:
#             return True
#         else:
#             return False
#
# karl = Person()
# print(karl.Tell_my_name)
# print(Person.is_adult(20))

#
# from datetime import date
# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     @classmethod
#     def fromBirthYear(cls,name,birthYear):
#         return cls(name,date.today().year - birthYear)
#
#     def display(self):
#         print(self.name + "'s age is:"+str(self.age))
#
# adam = Person('Adam',20)
# adam.display()
#
# sergey = Person.fromBirthYear('Sergey', 1960)
# sergey.display()


#
# from time import time
# def stopwatch(func):
#     def wrap():
#         print('Засекаем время')
#         t = time()
#         func()
#         print('Время выполнения:',time()-t)
#     return wrap
# def filter(func):
#     names = list()
#     def wrap(name):
#         if name in names:
#             print('Wrong name, try again')
#         else:
#             func(name)
#             names.append(name)
#     return wrap
# # @stopwatch
# @filter
# def say_hello(name):
#     print(f'hello, {name}')
# say_hello('Тимур')
# say_hello('Сергей')
# say_hello('Тимур')
#
# @stopwatch
# def try_time():
#     l = [i for i in range(1_000_000_00)]
#     for i in l:
#         if i:
#             pass
#
#
# def first_decorator(func):
#     def wrap():
#         print('______________________________')
#         print('Айтишник сейчас: ')
#         func()
#         print('Айтишник закончил дело')
#         print('______________________________')
#     return wrap
# @first_decorator
# def drink_coffe():
#     print(f'~~~~~~~~Пьёт кофе~~~~~~~')
#
#
# @first_decorator
# def write_code():
#     print('~~~~~~~~Пишет код~~~~~~~')
# # drink_coffe()
# # write_code()
#
# # it_doing(drink_coffe,write_code,drink_coffe,drink_coffe,drink_coffe)

# l = [i for i in range(1, 1001) if i % 30 == 0 or i % 31 == 0]
# def transform(x):
#      x = int(x)
#      return x**2
#
# new_list = list(map(lambda x: int(x)**2,input().split()))
#
# print(new_list)
# print(type(new_list[0]))



import sys
item_id = 0

class Item: #класс для товара
    def __init__(self,name,complete = " "): #[ ] - не куплен, [X] -куплен
        self.name = name
        self.complete = complete
        global item_id
        item_id +=1
        self.id = item_id

    def __str__(self):
        return f'Товар {self.name} c ID:{self.id}'


class ShoppingList: #класс - список покупок
    def __init__(self):
        self.shopping_list = []
        self.test = []

    def add_item(self):  #добавить товар в список покупок
        name = input('Введите название товара ')
        complete = " "
        self.shopping_list.append(Item(name,complete))


    def delete_item(self):
        print('Какой элемент удалить? ')
        n = int(input())
        for element in self.shopping_list:
            if element.id == n:
                self.shopping_list.remove(element)

    def show_list(self):
        print(' *   ID   Товар')
        for element in sorted(self.shopping_list, key = lambda x: x.name):
            print(f'[{element.complete}] {element.id}) {element.name}  ')

    def show_ready(self):
        print('Куплены товары:')
        print(' ID   Товар')
        for element in self.shopping_list:
            if 'X' in element.complete:
                print(f' {element.id}) {element.name}  ')

    def mark(self):
        print('Какой элемент отметить купленным?')
        n = int(input())
        for element in self.shopping_list:
            if element.id == n:
                element.complete = 'X'

    def show_menu(self):
        menu = """
        ##########################################
        Выберите команду:
        1. Показать все товары
        2. Добавить товар
        3. Отметить как купленный
        4. Удалить товар
        5. Показать купленные товары
        6. Выход
        ##########################################
        """
        print(menu)

    def action(self,n):
        if n == 1: return self.show_list()
        if n == 2: return self.add_item()
        if n == 3: return self.mark()
        if n == 4: return self.delete_item()
        if n == 5: return self.show_ready()
        if n == 6: return sys.exit()

    def call_action(self):
        n = int(input('Введите номер команды: '))
        self.action(n)

s = ShoppingList() #создадим список покупок
s.shopping_list= [Item('Арбуз'),Item('Бумага'),Item('Порошок')]
while True:
    s.show_menu()
    s.call_action()


#примерный вид списка покупок
"""
1. Морковь
2. Масло
3. Газировка

"""