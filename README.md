# Warehouse

Tietokantasovellus-harjoitustyö 2018-kesä-2. Aihe: Varastonhallinta.

[Heroku](https://tsoha-warehouse.herokuapp.com/)  
[Tietokantakaavio](https://github.com/hajame/warehouse/blob/master/documentation/WarehouseManagementDB.png)  
[Käyttäjätarinat (User stories)](https://github.com/hajame/warehouse/blob/master/documentation/user_stories.md)  


## Kuvaus

Aiheeni on varastonhallinta-tietokantasovellus, jonka avulla käyttäjä voi tarkastella eri varastojen tilannetta. Varastojen ylläpitäjä voi antaa käyttäjille oikeuksia tarkastella ja muokata varastojen sisältöä ja täyttötilannetta. 

### Toimintoja:
- Kirjautuminen
- Eri varastojen tilanteen ja tuotteiden tarkastelu
	- Tuotteen varastotilanteen listaaminen (tuotteen kappalemäärät kussakin varastossa) [yhteenvetokysely]
- Varaston lisääminen
- Varaston käyttäjäoikeuksien myöntäminen
- Tuotteen lisääminen
	- Jos jokin tuote vie enemmän tilaa kuin varastossa on kapasiteettia jäljellä, ei tuotetta lisätä.
- Tuotteen poistamien
- Varaston poistaminen


