class Animal:

    def init(self, name, species, legs):
        self.name = name
        self.species = species
        self.legs = legs


    def voice(self):
        print(f'{self.name} подает звуки жизни')


    def move(self):
        print(f'{self.name} подает принаки жизни')

class Dog(Animal):

    def init(self, name, bread, legs):
        super().init(name=name, legs=legs, species='Dog')
        self.bread = bread

    def bark(self):
        print(f'{self.bread} {self.name} лает что ли!')


class Bird(Animal):

    def init(self, name, species, wingspan):
        super().init(name=name, species=species, legs=2)
        self.wingspan = wingspan

    def fly(self):
        print(f'{self.species} {self.name} кружиться как истребитель'))
