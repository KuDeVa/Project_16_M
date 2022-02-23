class Volunteer:
    def __init__(self, name, city):
        self.name = name
        self.city = city

class InvitedPersons(Volunteer):
    def __init__(self, name, city, status):
        super().__init__(name, city)
        self.status = status
    def __str__(self):
        return f'{self.name}, г.{self.city}, статус: {self.status}'

v1 = InvitedPersons('Иванов Иван Иванович', 'Санкт-Петербург', 'Наставник')
v2 = InvitedPersons('Сорокин Сергей Викторович', 'Нижний-Новгород', 'Стажёр')
v3 = InvitedPersons('Петров Олег Николаевич', 'Ростов-на-Дону', 'Волонтёр')


print(v1)
print(v2)
print(v3)
