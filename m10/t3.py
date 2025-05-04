class Hissi:
    def __init__(self, akerros, ykerros, nytkerros):
        self.akerros = akerros
        self.ykerros = ykerros
        self.nyt = nytkerros

    def siirry_kerrokseen(self, kerros):
        while self.nyt < kerros:
            self.kerros_ylös()
            print(f"Hissi on kerroksessa: {self.nyt}")
        while self.nyt > kerros:
            self.kerros_alas()
            print(f"Hissi on kerroksessa: {self.nyt}")

    def kerros_ylös(self):
        self.nyt += 1

    def kerros_alas(self):
        self.nyt -= 1


class Talo:
    def __init__(self, akerros, ykerros):
        self.akerros = akerros
        self.ykerros = ykerros
        self.hissit = {}

        for i in range(1, 4):
            aloituskerros = int(input(f"Missä kerroksessa Hissi {i} on aluksi? (0-{self.ykerros}): "))
            self.hissit[i] = Hissi(self.akerros, self.ykerros, aloituskerros)

    def palohälytys(self):
        for hissin_numero in self.hissit:
            self.hissit[hissin_numero].siirry_kerrokseen(self.akerros)
            print(f"Hissi {hissin_numero} on nyt pohjakerroksessa.")


talo = Talo(0, 7)

print(f"Palohälytys!")
talo.palohälytys()
