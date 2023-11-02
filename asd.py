class Recipe:
    def __init__(self, name, ing):
        self.name=name
        self.ing=ing
    def print_ing(self):
        print(f'ingr:{self.name}')
        for i in self.ing:
            print('-',i)

    def cook(self):
        print(f'Сегодня мы готовим:{self.name}./n Спагетти болоньезе.Выполняем инструкцию по приготовлению блюда:{self.name}.n/ Спагетти болоньезе...Блюдо Спагетти болоньезе готово!')
spaghetti = Recipe("Спагетти болоньезе", ["Спагетти", "Фарш", "Томатный соус", "Лук", "Чеснок", "Соль"])

spaghetti.print_ingredients()
spaghetti.cook()
cake = Recipe("Кекс", ["Мука", "Яйца", "Молоко", "Сахар", "Сливочное масло", "Соль", "Ванилин"])
cake.print_ingredients()
cake.cook()


