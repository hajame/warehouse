# Warehouse

#### Tietokantasovellus-harjoitustyö 2018-kesä-2

### Aihe: varastonhallinta

Aiheeni on varastonhallintasovellus, jonka avulla käyttäjä voi tarkastella eri varastojen tilannetta.  

Käyttäjälle annetaan listaus hänen hallinnoimistaan  varastoista. Käyttäjä voi tarkastella varastojen sisältöä, täyttötilannetta ja etsiä tuotteita varastoista tuotteen nimellä. Haun tuloksena käyttäjä näkee, missä varastossa tuotetta on paljon ja missä vähän. Ylläpitäjän oikeuksilla käyttäjä voi antaa toisille käyttäjille oikeuksia tarkastella ja muokata eri varastoja ja niiden sisältöä.  


__Sovellus: https://tsoha-warehouse.herokuapp.com/__

### Testikäyttäjätunnukset 

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


## Toteutuneet ja toteutumattomat ominaisuudet

### Toteutuneet ominaisuudet

- Kirjautuminen ja uuden käyttäjän luominen.
- Eri varastojen tilanteen ja tuotteiden tarkastelu.
	- Listataan vain ne varastot joihin käyttäjällä on oikeus.
- Listaus varaston tuotteista.
	- Mahdollisuus poistaa koko tuotenimi varastosta tai muokata tuotteen määrää varastossa. 
- Varastotilanteen tarkastelu
	- Missä varastossa on kyseistä tuotetta. `yhteenvetokysely`
	- Missä varastossa on eniten/vähiten tuotetta. `yhteenvetokysely`
- Varaston lisääminen, poistaminen ja päivittäminen.
- Tuotteen lisääminen, poistaminen ja päivittäminen.
- Jos jokin tuote vie enemmän tilaa kuin varastossa on kapasiteettia jäljellä, ei tuotetta lisätä. 
- Saman tuotenimen lisääminen kahdesti lisää tuotteen määrää. 
- Varaston käyttäjäoikeuksien myöntäminen.

### Toteutumattomat ominaisuudet

- Pääkäyttäjäoikeuden myöntäminen.

