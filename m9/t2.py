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


auto = Auto("ABC-123", 142, 0, 0)


print (f"auton rekisterinumero: {auto.rtunnus}")
print (f"Auton huippunopeus: {auto.hnopeus}km/h")
print (f"Auton tämän hetkinen nopeus: {auto.nopeus}km/h")
print(f"Kuljettu matka: {auto.matka}m" )


auto.kiihdytä(30)
print(f"Auton nopeus kiihdytyksen jälkeen: {auto.nopeus} km/h")
auto.kiihdytä(70)
print(f"Auton nopeus kiihdytyksen jälkeen: {auto.nopeus} km/h")
auto.kiihdytä(50)
print(f"Auton nopeus kiihdytyksen jälkeen: {auto.nopeus} km/h")



auto.kiihdytä(-200)
print(f"Auton nopeus jarrutuksen jälkeen: {auto.nopeus} km/h")