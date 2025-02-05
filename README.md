# README – Selenium Testiranje za DemoBlaze

## Pregled
Ovaj projekt sadrži automatizirane **Selenium** testove za web stranicu **DemoBlaze**. Skripta testira funkcionalnosti poput prijave, dodavanja i uklanjanja artikala iz košarice, navigacije na početnu stranicu te odjave korisnika.

## O DemoBlaze stranici
[DemoBlaze](https://www.demoblaze.com/) je **dummy web trgovina** namijenjena za testiranje i vježbanje automatizacije testiranja. Stranica simulira funkcionalnosti e-trgovine, uključujući:
- Registraciju i prijavu korisnika
- Pregled proizvoda (laptopi, telefoni, monitori)
- Dodavanje proizvoda u košaricu
- Uklanjanje proizvoda iz košarice
- Proces kupnje

## Korišteni alati
Za izradu i izvođenje testova korišteni su sljedeći alati:
- **Python** – programski jezik korišten za pisanje testova.
- **Selenium WebDriver** – alat za automatizaciju web preglednika.
- **Google Chrome** – preglednik korišten za testiranje.
- **Chrome WebDriver** – potreban za kontrolu preglednika putem Seleniuma.

## Preduvjeti
Prije pokretanja skripte potrebno je instalirati **Selenium** pomoću sljedeće naredbe:

```bash
pip install selenium
