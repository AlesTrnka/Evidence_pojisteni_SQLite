# Evidence_pojisteni_SQLite
Aplikace k evidenci nových klientů pojišťovny se zaznamenáním údajů do databáze SQLite

Úvodní obrazovka aplikace umožňuje uživateli zvolit jednu z 5 operací:

1 - Přidat nového pojištěného
2 - Vypsat seznam pojištěných
3 - Vyhledat pojištěného a zobrazit podrobnosti
4 - Editovat pojištěnce
5 - Ukončit program

1 - Přidat nového pojištěného 
Aplikace postupně vyzve k zadání údajů o novém klientovi (jméno, příjmení, věk, email, telefon, ulice, město, PSČ).
Následně se vytvoří instance třídy Klient a údaje nového klienta jsou zaevidovány do databáze SQLite.

2 - Vypsat seznam pojištěných
Výpis seznamu klientů z databáze, limit 50.

3 - Vyhledat pojištěného a zobrazit podrobnosti
Vyhledání klienta v databázi podle zadaného jména a příjmení. Následně vypíše všechny údaje o klientovi.

4 - Editovat pojištěnce
Umožňuje změnit kterýkoliv údaj klienta v databázi.
