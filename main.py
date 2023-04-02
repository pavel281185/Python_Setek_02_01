class Robot:
    def __init__(self, baterie, delka_rukou):
        self.baterie = baterie
        self.delka_rukou = delka_rukou
        self.ukony_do_kontroly = 1000

    def krok_vpred(self):
        print("Robot udělal krok vpřed")
        self.ukony_do_kontroly -= 1
        print(f"Úkonů do kontroly {self.ukony_do_kontroly}")

    def krok_vzad(self):
        print("Robot udělal krok vzad")
        self.ukony_do_kontroly -= 1
        print(f"Úkonů do kontroly {self.ukony_do_kontroly}")

robor_1 = Robot(24, 0.6)

print(robor_1.baterie)
print(robor_1.delka_rukou)
print(robor_1.ukony_do_kontroly)

robor_1.krok_vpred()
print(robor_1.ukony_do_kontroly)
robor_1.krok_vzad()
print(robor_1.ukony_do_kontroly)

