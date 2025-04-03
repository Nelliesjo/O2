class Auto:
    def __init__(self, rtunnus, hnopeus, nopeus, matka):
        self.rtunnus = rtunnus
        self.hnopeus = hnopeus
        self.nopeus = nopeus
        self.matka = matka

auto = Auto("ABC-123", 142, 0, 0)


print (f"auton rekisterinumero: {auto.rtunnus}")
print (f"Auton huippunopeus: {auto.hnopeus}km/h")
print (f"Auton tämän hetkinen nopeus: {auto.nopeus}km/h")
print(f"Kuljettu matka: {auto.matka}km" )
