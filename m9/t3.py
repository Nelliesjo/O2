class Auto:
    def __init__(self, hnopeus, nopeus, matka):
        self.hnopeus = hnopeus
        self.nopeus = nopeus
        self.matka = matka

    def kiihdytä(self, muutos):
        uusnopeus = self.nopeus + muutos

        if uusnopeus > self.hnopeus:
            self.nopeus = self.hnopeus
        elif uusnopeus < 0:
            self.nopeus = 0
        else:
            self.nopeus = uusnopeus

    def kulje(self, tunnit):
        uusmatka = self.nopeus * tunnit
        self.matka =+ uusmatka + 2000


auto = Auto(142, 0, 0)

auto.kiihdytä(60)
auto.kulje(1.5)

print(f"Auton nopeus kiihdytyksen jälkeen: {auto.nopeus} km/h")
print(f"Auton kuljettu matka kiihdytyksen jälkeen: {auto.matka} km")
