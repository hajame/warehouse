# Käyttötapaukset (user stories)

Alla on kuvattuna varastonhallintasovellukselle olennaisia käyttäjätarinoita.

### Käyttäjänä...

1. Haluan tarkastella varastojen sisältöä ja kappalemääriä. [valmis]
    - Näen myös paljonko missäkin varastossa on tilaa jäljellä. [valmis]
2. Voin lisätä tai poistaa tuotteita varastosta nopeasti. [valmis]
    - Voin kirjoittaa uuden kappalemäärän, joka korvaa edellisen [valmis]
    - Voin klikata hiirellä yksittäisiä tuotepoistoja tai lisäyksiä [valmis]
    - Voin myös poistaa kaikki samaa nimeä edustavat tuotteet varastosta. [valmis]
3. Haluan luoda uusia varastoja. [valmis]
    - Haluan muokata omien varastojeni tietoja: nimeä ja kapasiteettia. [valmis]
4. Haluan saada tiedon tietyn tuotteen varastotilanteesta. [valmis]
    - Haluan listan varastoista, joissa kyseistä tuotetta on, ja tuotteen kappalemäärät. [valmis]
    - Haluan tietää, missä varastossa on eniten kyseistä tuotetta. [valmis]
        > Alla oleva haku listaa varastot, joissa tuotetta on suuruusjärjestyksessä:  
        > `SELECT DISTINCT warehouse.id, warehouse.name, warehouse_item.amount FROM warehouse, item, warehouse_item WHERE item.name = 'Flower pot' AND item.id = warehouse_item.item_id AND warehouse_item.warehouse_id = warehouse.id ORDER BY warehouse_item.amount DESC ;`
    
### Pääkäyttäjänä...

1. Haluan saada listan kaikista järjestelmän varastoista. [valmis]
2. Haluan antaa käyttäjille oikeuksia hallinoida varastoja. [valmis]
3. Haluan poistaa käyttäjiä. [valmis]
4. Haluan muokata käyttäjän tietoja, kuten nimeä, käyttäjätunnusta tai salasanaa [valmis]
