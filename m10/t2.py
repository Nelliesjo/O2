class Hissi:
    def __init__(self, akerros, ykerros):
        self.akerros = akerros
        self.ykerros = ykerros
        self.nyt = akerros

    def siirry_kerrokseen(self, kerros):
        while self.nyt < kerros:
            self.kerros_ylös()
            print(f"Hissi numero {hissin_numero} on kerroksessa: {self.nyt}")
        while self.nyt > kerros:
            self.kerros_alas()
            print(f"Hissi numero {hissin_numero} on kerroksessa: {self.nyt}")

    def kerros_ylös(self):
        self.nyt += 1

    def kerros_alas(self):
        self.nyt -= 1

class Talo:
    def __init__(self, akerros, ykerros, hissien_lkm):
        self.akerros = akerros
        self.ykerros = ykerros
        self.hissien_lkm = hissien_lkm
        self.hissit = {}

        for i in range(1, hissien_lkm + 1):
            self.hissit[i] = Hissi(self.akerros, self.ykerros)

    def aja_hissiä(self, hissin_numero, kerros):
        self.hissit[hissin_numero].siirry_kerrokseen(kerros)


kerros = int(input("Mihin kerrokseen haluat mennä?: "))
talo = Talo(0, 7, 3)

hissin_numero = int(input("Mitä hissiä haluat käyttää? (1-3): "))
talo.aja_hissiä(hissin_numero, kerros)
print("")
