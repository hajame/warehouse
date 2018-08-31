# Warehouse

#### Tietokantasovellus-harjoitustyö 2018-kesä-2

### Aihe: varastonhallinta

Aiheeni on varastonhallintasovellus, jonka avulla käyttäjä voi tarkastella eri varastojen tilannetta.  

Käyttäjälle annetaan listaus hänen hallinnoimistaan  varastoista. Käyttäjä voi tarkastella varastojen sisältöä, täyttötilannetta ja etsiä tuotteita varastoista tuotteen nimellä. Haun tuloksena käyttäjä näkee, missä varastossa tuotetta on paljon ja missä vähän. Ylläpitäjän oikeuksilla käyttäjä voi antaa toisille käyttäjille oikeuksia tarkastella ja muokata eri varastoja ja niiden sisältöä.  


__Sovellus: https://tsoha-warehouse.herokuapp.com/__

## Testikäyttäjätunnukset 

|	       |   admin       |   test        |   hello      |
|--------------|---------------|---------------|--------------|
| __PASSWORD__ | pass 	       | pass          | world        |
| __ROLE__     | ADMIN 	       | USER          | USER         |


## Dokumentaatio

- [Tietokantakaavio](https://github.com/hajame/warehouse/blob/master/documentation/images/WarehouseManagementDB.png)  
- [Käyttäjätarinat](https://github.com/hajame/warehouse/blob/master/documentation/user_stories.md)  
- [Käyttöohje](https://github.com/hajame/warehouse/blob/master/documentation/user_guide.md)  
- [Asennusohje](https://github.com/hajame/warehouse/blob/master/documentation/installation_guide.md)
- [Omat kokemukset](https://github.com/hajame/warehouse/blob/master/documentation/reflection_of_experiences.md)
- [SQL-CREATE TABLE -lauseet](https://github.com/hajame/warehouse/blob/master/documentation/SQL_CREATE_TABLE.md)


## Ominaisuudet

### Toteutuneet ominaisuudet

_Warehouse_ (CRUD)
- Varastojen listaaminen, lisääminen, poistaminen ja päivittäminen
- Saman tuotenimen lisääminen kahdesti lisää tuotteen määrää, ei uutta tuotetta
	- __Jos jokin tuote vie enemmän tilaa kuin varastossa on kapasiteettia__ jäljellä, ei tuotetta lisätä. `yhteenvetokysely`
- Eri varastojen tilanteen ja tuotteiden tarkastelu
	- Listaus varaston tuotteista
	- Listataan vain ne varastot joihin käyttäjällä on oikeus
	
	
_Item_ (CRUD)
- Tuotteiden listaaminen, lisääminen, poistaminen ja päivittäminen.
- Mahdollisuus poistaa koko tuotenimi varastosta tai muokata tuotteen määrää varastossa
- Tuotteen varastotilanteen tarkastelu
	- __Varastohaku tuotteen nimellä__: Missä varastossa on kyseistä tuotetta. `yhteenvetokysely`
	- __Missä varastossa on eniten/vähiten tuotetta__ `yhteenvetokysely`
	

_User_ (CRUD)
- Kirjautuminen ja uuden käyttäjän luominen
- Käyttäjän tietojen lukeminen, päivittäminen ja käyttäjän poistaminen `vain admin`
	- Käyttäjän poistaminen ei poista hänen hallitsemiaan varastoja
- Varaston käyttäjäoikeuksien myöntäminen

### Toteutumattomat ominaisuudet / Kehitysideat

- Pääkäyttäjäoikeuden myöntäminen.
- Käyttäjän haku nimellä
- Varaston haku nimellä
- Tuotehakuun haku nimen osalla ja välinpitämättömyys kirjainkoosta
- Sivutus tuotteiden, varastojen ja käyttäjien listauksessa
