class Student:
    def __init__(self, name, age, grade, score):
        self.name=name
        self.age=age
        self.grade=grade
        self.score=score

    def display(self):
        print(f'asd:{self.name}')
        print(f'asd:{self.age}')
        print(f'asdasd:{self.grade}')
        print(f'asdaxz:{self.score}')

    def avange_score(self):
        y = sum(self.score)
        c = len(self.score)
        return y / c



x = Student('asd',12, 12, [1, 2, 5,3] )
print(x.avange_score())
x.display()