class Dog:
    def __init__(self,name,age,coat_colour):
        self.name=name
        self.age=age
        self.coat_colour=coat_colour
        
    def description(self):
        print("Name :", self.name)
        print("Age :", self.age)
    
    def get_info(self):
        print("Coat Colour :", self.coat_colour)
        
class JackRussellTerrier(Dog):
    def __init__(self, name, age, coat_color):
        super().__init__(name, age, coat_color)

    def m1(self):
        print(self.name, "is Barking!")
        
    def m2(self):
        print(self.name, "is jumping!")


class Bulldog(Dog):
    def __init__(self, name, age, coat_color):
        super().__init__(name, age, coat_color)

    def m1(self):
        print(self.name, "is Running!")
        
    def m2(self):
        print(self.name, "is Snoring!")

D1 = Dog("Bruno", 3, "Brown")
D1.description()
D1.get_info()

D2 = JackRussellTerrier("Charlie", 2, "White")
D2.description()
D2.get_info()
D2.m1()
D2.m2()

D3 = Bulldog("Hunter", 4, "black")
D3.description()
D3.get_info()
D3.m1()
D3.m2()