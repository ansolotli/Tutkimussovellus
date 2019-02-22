# Tutkimussovellus

Kyseessä on sovellus, johon kerätään vesistöjen tilaan liittyviä tutkimustietoja. Sovellukseen voi tallentaa tutkimuspaikkoja, sekä eri paikoista otettuja näytteitä. Kerätyistä näytteistä kirjataan ylös näytteen tyyppi (esimerkiksi kasviplankton, eläinplankton, pohjaeläimet yms.) ja näytteestä löytyneet lajit, sekä niiden lukumäärä. Samasta paikasta voidaan ottaa useita näytteitä. Sovelluksessa voi myös tarkastella omaa tutkimusdataa, sillä sovellus listaa mm. näytteet, jotka tietty käyttäjä on lisännyt sovellukseen.

[Sovellus Herokussa](https://samplingapp.herokuapp.com/)

Sovellukseen voi kirjautua sisään testitunnuksilla: käyttäjänimi "testi", salasana "testi1".
Halutessaan voi myös luoda itselleen oman käyttäjätunnuksen, jolla kirjautua sisään.

## Sovelluksessa tällä hetkellä olevia toimintoja
- rekisteröityminen ja kirjautuminen
- tutkimuspaikan lisääminen, poistaminen ja muokkaaminen
- tutkimuspaikkojen haku paikannimien perusteella
- tutkimusnäytteen lisääminen, poistaminen ja muokkaaminen
- omien tutkimustietojen tarkastelu

Sovelluksen [tietokantakaavio](https://github.com/ansolotli/Tutkimussovellus/blob/master/documentation/pics/tsoha_database.jpg)

[Käyttötapaukset (user stories)](https://github.com/ansolotli/Tutkimussovellus/blob/master/documentation/userstories.md)

## Mahdollisia jatkokehitysideoita ja -tarpeita
- yksityiskohtaisempien tutkimustietojen tallentaminen
- tutkimuspaikan historiatietojen tarkastelu
- näytteen kommentointi
- laajemmat hakutoiminnallisuudet
- mahdollisuus tulostaa tietokannan hakutuloksia .csv-tiedostoina
