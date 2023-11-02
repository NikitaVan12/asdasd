class BankAccount:

    def init(self, balance, int_rate, trans, history):
        self.__balance = balance
        self.__int_rate = int_rate
        self.history = history
        self.__trans - trans

    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f'Внесение наличных на счет: {amount}')
        self.history.append('Внесение наличных')

    def withdraw(self,amount):
        self.balance = self.balance - amount
        print(f'Снятие наличных: {amount}')
        self.history.append('Снятие наличных')

    def add_interest(self):
        self.balance = self.balance * self.__int_rate / 100 + self.__balance
        print(f'Начисленны проценты по вкладу: {self.balance * self.int_rate / 100}')
        self.history.append('Начисление процентов')

    def history_list(self):
        for i in self.history:
            print("-", i)

account = BankAccount(1000000, 32432, 34231)
account.deposit(15000)
account.withdraw(7500)
account.add_interest()
account.history_list()
class Publisher:
    def init(self, name, location):
        self.name=name
        self.location=location

    def get_info(self):
        return f'издательства: {self.name},{self.location}'

    def publish(self,message):
        return f'Готовим:{message} к публикации в {self.name} ({self.location})'

class BookPublisher(Publisher):

    def init(self, name, locatiobn, num_authors ):
        super().init(name,locatiobn)
        self.num_authors = num_authors

    def publish(self,book, author):
        return f'Передаем рукопись,: {book} написанную автором:{author} в издательство:{self.name} ({self.location})'

class NewspaperPublisher(Publisher):

    def init(self, name, locatiobn, num_bages):
        super().init(name, locatiobn)
        self.num_pages=num_bages

    def publish(self,message):
        return (f'Печатаем свежий номер со статьей:{message} на главной странице в издательстве:{self.name} ({self.location})')


pub = Publisher('asdasd', 'alabuga')

print(pub.publish('asdasdzxc'))
print(pub.get_info())
book_publisher = BookPublisher("Важные Книги", "Самара", 52)
print(book_publisher.publish("Приключения Чебурашки", "В.И. Пупкин"))

newspaper_publisher = NewspaperPublisher("Московские вести", "Москва", 12)
print(newspaper_publisher.publish("Новая версия Midjourney будет платной"))



x = BankAccount('512', '0', '52')
x.display()
