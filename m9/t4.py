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

autot = []
for i in range(1, 11):
    rtunnus = f"ABC-{i}"
    hnopeus = random.randint(100, 200)
    auto = Auto(rtunnus, hnopeus, 0, 0)
    autot.append(auto)

while True:
    for auto in autot:
        auto.kiihdytä(random.randint(-10, 15))
        auto.kulje(1)

        if auto.matka >= 10000:
            print(f"{auto.rtunnus} on saavuttanut 10 000 km!")
            break
    else:
        continue
    break

print("Kilpailun tulokset:")
print(f"| Rekisteritunnus | Huippunopeus (km/h) | Nopeus (km/h) | Kuljettu matka (km) |")
print("-" * 79)
for auto in autot:
    print(f"      {auto.rtunnus:<20} {auto.hnopeus:<19} {auto.nopeus:<17} {auto.matka}")