class Auto:
    def __init__(self, rtunnus, hnopeus):
        self.rtunnus = rtunnus
        self.hnopeus = hnopeus
        self.nopeus = 0
        self.matka = 0

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


class Sähköauto(Auto):
    def __init__(self, rtunnus, hnopeus, akkukapasiteetti):
        super().__init__(rtunnus, hnopeus)
        self.akkukapasiteetti = akkukapasiteetti


class Polttomoottoriauto(Auto):
    def __init__(self, rtunnus, hnopeus, bensatankki):
        super().__init__(rtunnus, hnopeus)
        self.bensatankki = bensatankki


sahkoauto = Sähköauto("ABC-15", 180, 52.5)
polttisauto = Polttomoottoriauto("ACD-123", 165, 32.3)

sahkoauto.kiihdytä(150)
polttisauto.kiihdytä(200)

sahkoauto.kulje(3)
polttisauto.kulje(3)

print(f"Sähköauton ({sahkoauto.rtunnus}) kuljettu matka: {sahkoauto.matka} km")
print(f"Polttomoottoriauton ({polttisauto.rtunnus}) kuljettu matka: {polttisauto.matka} km")
