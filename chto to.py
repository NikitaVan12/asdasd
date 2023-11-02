class Publication:

    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def display(self):
        print('На', self.title)
        print(f'asd: {self.author}')
        print(f'asd: {self.year}')


class Magazine(Publication):

    def __init__(self, title, author, year, issume_number):
        super().__init__(title, author, year)
        self.issume_number = issume_number

    def display(self):
        super().display()
        print(f'asd: {self.issume_number}')


# p = Publication ('ajsfd', 'kajs', 'hdka')
# p.display()
m = Magazine('cheburashka', 'narodnay', 1995, 413248174)
m.display()
