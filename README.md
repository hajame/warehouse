# Warehouse

Tietokantasovellus-harjoitustyö 2018-kesä-2. 

Aihe: Varastonhallinta.  


## Varastonhallintasovellus

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

- [Tietokantakaavio](https://github.com/hajame/warehouse/blob/master/documentation/images/WarehouseManagementDB.png)  
- [Käyttäjätarinat](https://github.com/hajame/warehouse/blob/master/documentation/user_stories.md)  
- [Käyttöohje](https://github.com/hajame/warehouse/blob/master/documentation/user_guide.md)  
- [Asennusohje](https://github.com/hajame/warehouse/blob/master/documentation/installation_guide.md)


### Toimintoja

- Kirjautuminen ja uuden käyttäjän luominen. `valmis`
- Eri varastojen tilanteen ja tuotteiden tarkastelu. `valmis`
	- Listataan vain ne varastot joihin käyttäjällä on oikeus. `valmis`
- Listaus varaston tuotteista. `valmis`
	- Mahdollisuus poistaa koko tuotenimi varastosta tai muokata tuotteen määrää varastossa. `valmis`
- Missä varastossa on kyseistä tuotetta [yhteenvetokysely] `valmis`
	- Missä varastossa on eniten/vähiten tuotettta [yhteenvetokysely] `ei toteutettu`
- Varaston lisääminen, poistaminen ja päivittäminen. `valmis`
- Varaston käyttäjäoikeuksien myöntäminen. `ainoastaan varastoa luodessa`
- Tuotteen lisääminen, poistaminen ja päivittäminen. `toteutettu osin`
	- Jos jokin tuote vie enemmän tilaa kuin varastossa on kapasiteettia jäljellä, ei tuotetta lisätä. `valmis`
	- Saman tuottenimen lisääminen kahdesti lisää tuotteen määrää. `valmis`
