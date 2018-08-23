# Warehouse - Käyttöohje

Sovellusta voi käyttää paikallisesti osoitteessa <http://localhost:5000>, tai haluamassan web-hostauspalvelussa: sovellus pyörii tällä hetkellä esimerkiksi osoitteessa <http://tsoha-warehouse.herokuapp.com/>.

## Kirjautuminen

Sovelluksen luoma sivusto on suojattu salasanalla, jotta ulkopuoliset eivät pääse sitä lukemaan. Heroku-sovellukseen on määritelty valmiiksi käyttäjätilejä, jotka ovat sovelluksen testikäytön kannalta käteviä. Nämä tilit ovat:

| Käyttäjätunnus   | Salasana   | Käyttäjärooli |
| ---------------- | ---------- | ------------- |
| admin            | pass       | ADMIN         |
| test             | pass       | USER          |
| hello            | world      | USER          |

Sovellukseen on mahdollista luoda uusia käyttäjiä. Kirjautuminen on helppoa, kirjautumaton käyttäjä ohjataan kirjautumissivulle __Log in__ -linkistä. 

Voit kirjautua ulos koska vaan valitsemalla __Log out__-linkin.

## Rekisteröityminen

Luo uusi käyttäjä painamalla linkkiä __Register__.

Syötä kenttiin pyydetyt tiedot ja ota huomioon nimimerkeille ja salasanoille annetut rajoitteet. Korjaa tarvittaessa syötteesi virheilmoitusten ilmoittamista virheistä. Rekisteröinnin onnistumisen jälkeen sovellus ohjaa käyttäjän kirjautumisnäkymään.

## Etusivu

Kirjautuessasi sovellukseen sinut ohjataan etusivulle, jossa on listattuna varastojen ja tuotteiden kokonaismäärät.

![etusivu](https://github.com/hajame/warehouse/blob/master/documentation/images/index.png)  

Etusivulle pääsee palaamaan muista sovelluksen näkymisetä klikkaamalla navigaatiopalkin vasemmassa yläreunassa olevasta __Warehouse__ nimestä.

## Warehouses 

![warehouses](https://github.com/hajame/warehouse/blob/master/documentation/images/warehouses.png)  

- __varastojen tarkastelu__
    - __Warehouses__ linkistä näet ne varastot, joihin käyttäjälläsi on käyttöoikeudet.
    - valitse __view__ tarkastellaksesi varaston _tietoja ja tuotteita_.  

- __varaston muokkaaminen__
    - valitse __edit__ muokataksesi varaston _nimeä_ tai _tilavuutta_  
    - valitse __delete__ poistaaksesi varaston. Yhteydet varaston ja tuotteiden väliltä poistetaan.  

- __varaston tuotteiden muokkaaminen__
    - lisää tai poista yksi tuote __klikkaamalla +/-__
    - poista tuote varastosta valitsemalla __delete__ tuotteen vierestä


## Add a warehouse - varaston lisääminen

Anna varastolle uniikki __nimi__ ja __tilavuus__ väliltä 0-2147483647. Tilavuuden yksikkö on käyttäjän pään sisällä. Valitse __Add a new warehouse__ lisätäksesi varaston.

## Add an item - tuotteiden lisääminen varastoihin

![lisää tuote](https://github.com/hajame/warehouse/blob/master/documentation/images/add_item.png)  

1. Kirjoita tuotteen nimi kenttään __Name__.  
2. Kirjoita tuotteen tilavuus kenttään __Volume__.
3. Kirjoita lisättävä määrä kenttään __Amount__.
4. Kirjoita olemassa olevan varaston nimi kenttään __Warehouse__.

Varastoihin tuotteita lisätessä on syytä muistaa, että jos tuote on jo olemassa, sille ei voi määrittää eri tilavuutta (volume).

Jos varastossa on esimerkiksi tuote 'Vehnäjauho', tilavuus: 5, määrä 1.
Tällöin tuotteen 'Vehnäjauho', tilavuus: 10 lisääminen lisää vain edellisen tuotteen määrää varastossa, eikä muuta tuotteen tilavuutta.  

On suositeltavaa lisätä eri kokoisten pakkausten pakkauskoot suoraan tuotteen nimeen:  

| name                  | volume |
| ----------------------| ------ |
| 'Vehnäjauho (5kg)'    | 5      |
| 'Vehnäjauho (10kg)'   | 10     |


## List all items 

![listaa tuotteet](https://github.com/hajame/warehouse/blob/master/documentation/images/list_all_items.png)  

- listaa tuotteet ja hae tuotteen nimellä  

Sivu listaa jokaisen järjestelmään lisätyn tuotteen ja sen tilavuuden.  

- Selvitä, missä varastoissa on tiettyä tuotetta kirjoittamalla tuotteen nimi __Name__ kenttään ja valitse __search__.

## Järjestelmänvalvojan (admin) työkalut

### All warehouses - listaa kaikki varastot

Järjestelmänvalvojalla on oikeus tarkastella ja muokata kaikkia varastoja. Valitse navigaatiopalkista __All warehouses__ listataksesi kaikki varastot. Näkymää käytetään [Warehouses](https://github.com/hajame/warehouse/blob/master/documentation/user_guide.md#warehouses) -näkymän tavoin.

## Uloskirjautuminen

Voit kirjautua ulos koska vaan valitsemalla __Log out__-linkin.
