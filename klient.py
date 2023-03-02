class Klient:
    """ Třída pro vytvoření nových pojištěných (instancí) """
    
    def __init__(self, jmeno, prijmeni, vek, email, telefon, ulice, mesto, psc):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.vek = vek
        self.email = email
        self.cislo = email
        self.telefon = telefon
        self.ulice = ulice
        self.mesto = mesto
        self.psc = psc
    def __str__(self):
        return (f"{self.jmeno}\t{self.prijmeni}\t{self.vek}\t{self.telefon}")