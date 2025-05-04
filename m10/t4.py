import random


class Auto:
    def __init__(self, rtunnus, hnopeus, nopeus, matka):
        self.rtunnus = rtunnus
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
        self.matka += self.nopeus * tunnit


class Kilpailu:
    def __init__(self, pituus, autot):
        self.pituus = pituus
        self.autot = autot

    def tunti_kuluu(self):
        for auto in self.autot:
            muutos = random.randint(-10, 15)
            auto.kiihdytä(muutos)
            auto.kulje(1)

    def tulosta_tilanne(self):
        print("-" * 79)
        print(f"| Rekisteritunnus | Huippunopeus (km/h) | Nopeus (km/h) | Kuljettu matka (km) |")
        print("-" * 79)
        for auto in self.autot:
            print(f"      {auto.rtunnus:<20} {auto.hnopeus:<19} {auto.nopeus:<17} {auto.matka}")

    def kilpailu_ohi(self):
        for auto in self.autot:
            if auto.matka >= self.pituus:
                print(f"{auto.rtunnus} on saavuttanut {self.pituus} km ja voitti kilpailun!")
                return True
        return False


autot = []
for i in range(1, 11):
    rtunnus = f"ABC-{i}"
    hnopeus = random.randint(100, 200)
    auto = Auto(rtunnus, hnopeus, 0, 0)
    autot.append(auto)

print(f"Suuri romuralli")
kilpailu = Kilpailu( 8000, autot)

tunti = 0
while True:
    kilpailu.tunti_kuluu()
    tunti += 1

    if tunti % 10 == 0:
        kilpailu.tulosta_tilanne()

    if kilpailu.kilpailu_ohi():
        break
