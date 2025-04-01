class Ksiazka:
    def __init__(self, tytul, autor, rok_wydania):
        self.tytul = tytul
        self.autor = autor
        self.rok_wydania = rok_wydania

    def opis(self):
        return f"'{self.tytul}' - {self.autor}, {self.rok_wydania}"


class Ebook(Ksiazka):
    def __init__(self, tytul, autor, rok_wydania, rozmiar_pliku):
        super().__init__(tytul, autor, rok_wydania)
        self.rozmiar_pliku = rozmiar_pliku

    def opis(self):
        return f"{super().opis()} (Wielkość pliku: {self.rozmiar_pliku}MB)"


class Audiobook(Ksiazka):
    def __init__(self, tytul, autor, rok_wydania, czas_trwania):
        super().__init__(tytul, autor, rok_wydania)
        self.czas_trwania = czas_trwania

    def opis(self):
        return f"{super().opis()} (Czas trwania: {self.czas_trwania} min)"


ksiazka1 = Ksiazka("Wiedźmin", "Andrzej Sapkowski", 1999)
ebook1 = Ebook("Wiedźmin", "Andrzej Sapkowski", 2010, 58)
audiobook1 = Audiobook("Wiedźmin", "Andrzej Sapkowski", 2012, 659)

print(ksiazka1.opis())
print(ebook1.opis())
print(audiobook1.opis())