# Третьяков Роман Викторович
# Факультет Geek University Python-разработки. Основы языка Python
# Урок 7. Задание 2:
# Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная
# сущность (класс) этого проекта — одежда, которая может иметь определенное название. К типам
# одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
# размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
#
# Для определения расхода ткани по каждому типу одежды использовать формулы: для
# пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
#
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке
# знания: реализовать абстрактные классы для основных классов проекта, проверить на практике
# работу декоратора @property.

from abc import ABC, abstractmethod

class clothes(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_cloth_count(self):
        pass

class coat(clothes):

    def __init__(self, v):
        self.v = v

    @property
    def get_cloth_count(self):
        return self.v/6.5 + 0.5

class suit(clothes):

    def __init__(self, h):
        self.h = h

    @property
    def get_cloth_count(self):
        return self.h * 2 + 0.3


c1 = coat(52)
print(c1.get_cloth_count)

c2 = coat(56)
print(c2.get_cloth_count)


s1 = suit(164)
print(s1.get_cloth_count)

s2 = suit(172)
print(s2.get_cloth_count)