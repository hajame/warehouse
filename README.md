# Warehouse

Tietokantasovellus-harjoitustyö 2018-kesä-2. 

Aihe: Varastonhallinta.  


## Kuvaus

Aiheeni on varastonhallinta-tietokantasovellus, jonka avulla käyttäjä voi tarkastella eri varastojen tilannetta. Käyttäjälle annetaan listaus hänen hallinnoimistaan varastoista. Käyttäjä voi tarkastella varastojen sisältöä ja tehdä hakuja eri tuotteisiin. Ylläpitäjän oikeiuksilla käyttäjä voi antaa toisille käyttäjille oikeuksia tarkastella ja muokata eri varastoja ja niiden sisältöä. 


[Heroku](https://tsoha-warehouse.herokuapp.com/)  
[Tietokantakaavio](https://github.com/hajame/warehouse/blob/master/documentation/WarehouseManagementDB.png)  
[Käyttäjätarinat (User stories)](https://github.com/hajame/warehouse/blob/master/documentation/user_stories.md)  
[Käyttöohje](https://github.com/hajame/warehouse/blob/master/documentation/user_guide.md)


```
Testikäyttäjätunnukset 
-----------------------

(käyttäjille näytetään erilaiset varastolistaukset)

Username: test
Password: pass

----------------

Username: hello
Password: world

```  

### Toimintoja:
- Kirjautuminen ja uuden käyttäjän luominen
- Eri varastojen tilanteen ja tuotteiden tarkastelu
	- Listaus varaston tuotteista
	- Tietyn tuotteen kappalemäärät kussakin varastossa
	- Missä varastossa on kyseistä tuotetta eniten/vähiten [yhteenvetokysely]
- Varaston lisääminen, poistaminen ja päivittäminen
- Varaston käyttäjäoikeuksien myöntäminen
- Tuotteen lisääminen, poistaminen ja päivittäminen
	- Jos jokin tuote vie enemmän tilaa kuin varastossa on kapasiteettia jäljellä, ei tuotetta lisätä.
