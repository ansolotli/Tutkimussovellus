# Tutkimussovellus

Kyseessä on sovellus, johon kerätään vesistöjen tilaan liittyviä tutkimustietoja. Sovellukseen voi tallentaa tutkimuspaikkoja, sekä eri paikoista otettuja näytteitä. Kerätyistä näytteistä kirjataan ylös näytteen tyyppi (esimerkiksi kasviplankton, eläinplankton, pohjaeläimet tms.) ja näytteestä löytyneet lajit, sekä niiden lukumäärä. Samasta paikasta voidaan ottaa useita näytteitä. Sovelluksessa voi myös tarkastella omaa tutkimusdataa, sillä sovellus listaa mm. näytteet, jotka tietty käyttäjä on lisännyt sovellukseen.

### Sovelluksessa tällä hetkellä olevia toimintoja
- rekisteröityminen ja kirjautuminen
- tutkimuspaikan tarkastelu, lisääminen, poistaminen ja muokkaaminen
- tutkimuspaikkojen haku paikannimien perusteella
- näytteen tarkastelu, lisääminen, poistaminen ja muokkaaminen
- omien tutkimustietojen tarkastelu
- sovellukseen tallennettujen tietojen tarkastelu

### Dokumentaatiolinkit

- [asennusohje](https://github.com/ansolotli/Tutkimussovellus/blob/master/documentation/asennusohje.md)
- [käyttöohje toteutuneille toiminnallisuuksille](https://github.com/ansolotli/Tutkimussovellus/blob/master/documentation/kayttoohje.md)
- [Tietokantakaavio ja CREATE TABLE -lauseet](https://github.com/ansolotli/Tutkimussovellus/blob/master/documentation/tietokanta.md)
- [Käyttötapaukset (user stories) ja niihin liittyvät SQL-kyselyt](https://github.com/ansolotli/Tutkimussovellus/blob/master/documentation/userstories.md)

### Sovellus Herokussa

- [Herokuun](https://samplingapp.herokuapp.com/)

Sovellukseen voi kirjautua sisään testitunnuksilla: käyttäjänimi "testi", salasana "testi1".
Halutessaan voi myös luoda itselleen oman käyttäjätunnuksen, jolla kirjautua sisään.

### Mahdollisia jatkokehitysideoita ja -tarpeita
- yksityiskohtaisempien tutkimustietojen tallentaminen
- tutkimuspaikan historiatietojen tarkastelu
- näytteen kommentointi
- laajemmat hakutoiminnallisuudet
- mahdollisuus tulostaa tietokannan hakutuloksia .csv-tiedostoina
