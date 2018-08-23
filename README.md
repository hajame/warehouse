# Warehouse

Tietokantasovellus-harjoitustyö 2018-kesä-2. 

Aihe: Varastonhallinta.  


## Varastonhallintasovellus:

Aiheeni on varastonhallintasovellus, jonka avulla käyttäjä voi tarkastella eri varastojen tilannetta.  

Käyttäjälle annetaan listaus hänen hallinnoimistaan  varastoista. Käyttäjä voi tarkastella varastojen sisältöä ja tehdä hakuja eri tuotteisiin. Ylläpitäjän oikeuksilla käyttäjä voi antaa toisille käyttäjille oikeuksia tarkastella ja muokata eri varastoja ja niiden sisältöä.  


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

### Dokumentaatio

- [Tietokantakaavio](https://github.com/hajame/warehouse/blob/master/documentation/WarehouseManagementDB.png)  
- [Käyttäjätarinat (User stories)](https://github.com/hajame/warehouse/blob/master/documentation/user_stories.md)  
- [Käyttöohje](https://github.com/hajame/warehouse/blob/master/documentation/user_guide.md)  
- [Asennusohje](https://github.com/hajame/warehouse/blob/master/documentation/installation_guide.md)


### Toimintoja:

- Kirjautuminen ja uuden käyttäjän luominen
- Eri varastojen tilanteen ja tuotteiden tarkastelu
	- Listataan vain ne varastot joihin käyttäjällä on oikeus
- Listaus varaston tuotteista
	- Listaus varastoista joissa on tietynnimistä tuotetta ja minkä verran
	- Missä varastossa on kyseistä tuotetta eniten/vähiten [yhteenvetokysely]
- Varaston lisääminen, poistaminen ja päivittäminen
- Varaston käyttäjäoikeuksien myöntäminen
- Tuotteen lisääminen, poistaminen ja päivittäminen
	- Jos jokin tuote vie enemmän tilaa kuin varastossa on kapasiteettia jäljellä, ei tuotetta lisätä.
