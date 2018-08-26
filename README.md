# Warehouse

Tietokantasovellus-harjoitustyö 2018-kesä-2. 

Aihe: Varastonhallinta.  


## Varastonhallintasovellus

Aiheeni on varastonhallintasovellus, jonka avulla käyttäjä voi tarkastella eri varastojen tilannetta.  

Käyttäjälle annetaan listaus hänen hallinnoimistaan  varastoista. Käyttäjä voi tarkastella varastojen sisältöä ja hakea tuotteita varastoista tuotteen nimellä. Ylläpitäjän oikeuksilla käyttäjä voi antaa toisille käyttäjille oikeuksia tarkastella ja muokata eri varastoja ja niiden sisältöä.  


__Sovellus: https://tsoha-warehouse.herokuapp.com/__

```
Testikäyttäjätunnukset 
-----------------------

Username: admin
Password: pass
----------------
Username: test
Password: pass
----------------
Username: hello
Password: world

```  

## Dokumentaatio

- [Tietokantakaavio](https://github.com/hajame/warehouse/blob/master/documentation/images/WarehouseManagementDB.png)  
- [Käyttäjätarinat](https://github.com/hajame/warehouse/blob/master/documentation/user_stories.md)  
- [Käyttöohje](https://github.com/hajame/warehouse/blob/master/documentation/user_guide.md)  
- [Asennusohje](https://github.com/hajame/warehouse/blob/master/documentation/installation_guide.md)
- [Omat kokemukset](https://github.com/hajame/warehouse/blob/master/documentation/reflection_of_experiences.md)


## Toteutuneet ja toteutumattomat ominaisuudet

### Toteutuneet ominaisuudet

- Kirjautuminen ja uuden käyttäjän luominen.
- Eri varastojen tilanteen ja tuotteiden tarkastelu.
	- Listataan vain ne varastot joihin käyttäjällä on oikeus.
- Listaus varaston tuotteista.
	- Mahdollisuus poistaa koko tuotenimi varastosta tai muokata tuotteen määrää varastossa. 
- Missä varastossa on kyseistä tuotetta- `yhteenvetokysely`
- Varaston lisääminen, poistaminen ja päivittäminen. 
- Jos jokin tuote vie enemmän tilaa kuin varastossa on kapasiteettia jäljellä, ei tuotetta lisätä. 
- Saman tuottenimen lisääminen kahdesti lisää tuotteen määrää. 

### Toteutumattomat ominaisuudet

- Missä varastossa on eniten/vähiten tuotetta. `yhteenvetokysely` `ei toteutettu`
- Tuotteen lisääminen, poistaminen ja päivittäminen. `toteutettu osin`
- Varaston käyttäjäoikeuksien myöntäminen. `ainoastaan varastoa luotaessa`
