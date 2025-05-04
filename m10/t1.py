class Hissi:
    def __init__(self, akerros, ykerros):
        self.akerros = akerros
        self.ykerros = ykerros
        self.nyt = akerros

    def siirry_kerrokseen(self, kerros):
        print(f"Ylöspäin.")
        while self.nyt < kerros:
            self.kerros_ylös()
            print(f"Kerros: {self.nyt}")
        print(f"Alaspäin.")
        while self.nyt > 0:
            self.kerros_alas()
            print(f"Kerros: {self.nyt}")


    def kerros_ylös(self):
        self.nyt = self.nyt + 1

    def kerros_alas(self):
        self.nyt = self.nyt - 1

hissi = Hissi(0, 7)

sijainti = int(input("Valitse kerros: "))
if sijainti <= hissi.ykerros:
    hissi.siirry_kerrokseen(sijainti-1)
else:
    print("Kerrosta ei ole.")