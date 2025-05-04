class Julkaisu:
    def __init__(self,nimi):
        self.nimi = nimi
    def tulosta_info(self):
        print(f"julkaisu: {self.nimi}")


class Kirja(Julkaisu):
    def __init__(self,nimi, kirjottaja, sivut):
        super().__init__(nimi)
        self.kirjottaja = kirjottaja
        self.sivut = sivut

    def tulosta_info(self):
        super().tulosta_info()
        print(f"Kirjottaja: {self.kirjottaja}")
        print(f"Sivujen määrä: {self.sivut}")


class Lehti(Julkaisu):
    def __init__(self,nimi,ptoimittaja):
        super().__init__(nimi)
        self.ptoimittaja = ptoimittaja

    def tulosta_info(self):
        super().tulosta_info()
        print(f"Päätoimittaja: {self.ptoimittaja} ")

if __name__ == "__main__":
    lehti = Lehti("Aku Ankka", "Aki Hyyppä")
    kirja = Kirja("Hytti n:o 6", "Rosa Liksom", 200)

    print(f"Lehden tiedot:")
    lehti.tulosta_info()

    print("kirjan tiedot:")
    kirja.tulosta_info()