class User:
    def __init__(self, surname, name, patronymic):
        self.surname = surname
        self.name = name
        self.patronymic = patronymic


class Client(User):
    def __init__(self, surname, name,patronymic, balance = 0):
        self.balance = balance

        User.__init__(self, surname, name, patronymic)

    def check_balance(self):
        print('Клиент "' + self.surname, self.name , self.patronymic + '". Баланс: ' + str(self.balance) + ' руб.\n')



if __name__ == '__main__':
    user1 = Client('Семенов', "Игорь", 'Петрович', 50)
    user2 = Client('Ветров', 'Евгений', 'Сергеевич', 130)
    user3 = Client('Стеклов', 'Петр', 'Семенович', 250)
    users = [user1, user2, user3,]
    print('----------------------------------------')
    for user in users:
        Client.check_balance(user)