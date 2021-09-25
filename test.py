class Mensch:
    def __init__(self, name ,leben, speed, iq, beauty) -> None:
        self.leben = leben
        self.speed = speed
        self.name = name
        self.iq = iq
        self.position = 0
        self.beauty = beauty

    def say_hello(self):
        print(f"I am a human, Hello! I am {self.name}")

    def move(self):
        self.position = self.position + self.speed
        print(f"My position is {self.position}")

class Student(Mensch):
    def __init__(self, grad_year, name, leben, speed, iq, beauty):
        super().__init__(name, leben, speed, iq, beauty)
        self.grad_year = grad_year

    def say_information(self):
        print(self.leben, self.speed, self.iq, self.grad_year)


    
jan = Student(12, "Jan", 123,213,123,123)
jan.say_information()
jan.say_hello()
hendrik = Mensch("Hendik", 10, 1111, 7, 314)
nick = Mensch("Nick", 11, 11, 8, 2184)
