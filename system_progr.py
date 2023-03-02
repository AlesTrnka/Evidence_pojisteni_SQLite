from evidence import Evidence
import os

pojistenci = Evidence()

def spustit_vse():
    pojistenci.vytvor_tabulku()
    while True:
        os.system('cls')
        print("Vítejte v aplikaci EVIDENCE POJIŠTĚNÍ\n")
        pojistenci.vypis_operace()
        volba = input("\nZadejte volbu:\t")
        if volba == "1":
            os.system('cls')
            print("Přidání nového klienta")
            print("ˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇ\n")
            jmeno = input("Zadejte křestní jméno:\n").capitalize()
            prijmeni = input("Zadejte příjmení:\n").capitalize()
            vek = input("Zadejte věk:\n")
            email = input("Zadejte e-mail:\n")
            telefon = input("Zadejte telefonní číslo:\n")
            ulice = input("Zadejte ulici bydliště a číslo popisné:\n")
            mesto = input("Zadejte město bydliště\n").capitalize()
            psc = input("Zadejte poštovní směrovací číslo:\n")
            pojistenci.pridej(jmeno, prijmeni, vek, email, telefon, ulice, mesto, psc)
            print("\nPojištěnec byl zaevidován do databáze.")
            input("Pokračujte klávesou Enter. . .")
        elif volba == "2":
            os.system('cls')
            print("Výpis pojištěnců z databáze (limit - 50):\n")
            print("ID / Jméno / Příjmení , Věk:")
            pojistenci.vypis_klienty()
            input("\nPokračujte klávesou Enter. . .")
        elif volba == "3":
            os.system('cls')
            print(f"VYHLEDÁNÍ POJIŠTĚNÉHO")
            print("ˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇ\n")
            jmeno = input("Zadejte křestní jméno:\n").capitalize()
            prijmeni = input("Zadejte příjmení:\n").capitalize()
            os.system('cls')
            print(f"Pro zadané jméno {jmeno} {prijmeni} jsou nalezeny tyto záznamy:\n")
            print("\nID / Jméno / Příjmení , Věk / Email, Telefon, Ulice a ČP, Město, PSČ")
            print("ˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇ")
            pojistenci.vyhledej(jmeno, prijmeni)     # Vyhledá klienta podle jména a příjmení
            input("\nPokračujte klávesou Enter. . .")
        elif volba == "4":
            os.system('cls')
            print(f"EDITACE POJIŠTĚNÉHO")
            print("ˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇ\n")
            jmeno = input("Zadejte jméno člověka, kterého chcete editovat:\n").capitalize()
            prijmeni = input("Zadejte příjmení člověka, kterého chcete editovat:\n").capitalize()
            udaj = input("Který údaj chcete aktualizovat? (jméno, příjmení, vek, email, telefon, ulice_ČP, město, PSČ)\n").lower()
            hodnota = input("Napište novou hodnotu:\t")
            pojistenci.edituj(jmeno, prijmeni, udaj, hodnota)
            print("Pojištěnec má nyní v databázi tyto údaje :\n")
            print("\nID / Jméno / Příjmení , Věk / Email, Telefon, Ulice a ČP, Město, PSČ")
            pojistenci.vyhledej(jmeno, prijmeni)
            input("\nPokračujte klávesou Enter. . .")
        elif volba == "5":
            os.system('cls')
            print("Přeji hezký den.")
            input("\nUkončete klávesou Enter. . .")
            return False
        else:
            print("Neplatné zadání, zvolte mezi čísly 1 až 5.")
            input("\nPokračujte klávesou Enter. . .")
            
    
