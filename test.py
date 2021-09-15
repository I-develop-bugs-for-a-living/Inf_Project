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

    

hendrik = Mensch("Hendik", 10, 1111, 7, 314)
nick = Mensch("Nick", 11, 11, 8, 2184)

while True:
    a = input()
    hendrik.move()

class Deutscher(Mensch):
    def say_goodbye():
        pass