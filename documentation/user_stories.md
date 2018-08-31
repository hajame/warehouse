# Käyttötapaukset (user stories)

Alla on kuvattuna varastonhallintasovellukselle olennaisia käyttäjätarinoita.

### Käyttäjänä...

1. Haluan tietää ilman kirjautumista, montako varastoa ja tuotetta järjestelmässä on.
    > `SELECT COUNT(warehouse.id) FROM warehouse`  
    > `SELECT COUNT(item.id) FROM item`
1. Haluan tarkastella varastojen sisältöä ja kappalemääriä. `valmis`
    - Näen myös paljonko missäkin varastossa on tilaa jäljellä. `valmis`
        > `SELECT SUM(warehouse_item.amount * item.volume) FROM warehouse_item, item WHERE warehouse_id = '1' AND warehouse_item.item_id = item.id;)`
2. Voin lisätä tai poistaa tuotteita varastosta nopeasti. `valmis`
    - Voin kirjoittaa uuden kappalemäärän, joka korvaa edellisen `valmis`
        > `UPDATE warehouse_item SET amount = 200 WHERE warehouse_id = 1 AND item_id = 2;`
    - Voin klikata hiirellä yksittäisiä tuotepoistoja tai lisäyksiä `valmis`
        - Kahdessa edellisessä minun ei tarvitse erikseen tarkistaa, mahtuuko lisätty tuote varastoon:
            > Tarkistetaan, paljonko varastossa on tilaa (kohta 2.) ja verrataan lisättävää tuotemäärää varaston tilavuuteen.  
            `SELECT volume FROM warehouse WHERE warehouse.id =  '1' ;`
    - Voin myös poistaa kaikki samaa nimeä edustavat tuotteet varastosta. `valmis`
3. Haluan luoda uusia varastoja. `valmis`
    - Haluan muokata omien varastojeni tietoja: nimeä ja kapasiteettia. `valmis`
            > `UPDATE warehouse SET name = 'Foo' WHERE id = 1;`
4. Haluan saada tiedon tietyn tuotteen varastotilanteesta. `valmis`
    - Haluan listan varastoista, joissa kyseistä tuotetta on, ja tuotteen kappalemäärät. `valmis`
    - Haluan tietää, missä varastossa on eniten kyseistä tuotetta. `valmis`
        > Alla oleva kysely listaa varastot, joissa tuotetta on, tuotemäärään nähden suuruusjärjestyksessä. Se toteuttaa kaksi edellistä käyttäjätapausta:  
        > `SELECT DISTINCT warehouse.id, warehouse.name, warehouse_item.amount FROM warehouse, item, warehouse_item WHERE item.name = 'Flower pot' AND item.id = warehouse_item.item_id AND warehouse_item.warehouse_id = warehouse.id ORDER BY warehouse_item.amount DESC ;`
    
### Pääkäyttäjänä...

1. Haluan saada listan kaikista järjestelmän varastoista. `valmis`
    > `SELECT * FROM warehouse;`
2. Haluan antaa käyttäjille oikeuksia hallinoida varastoja. `valmis`
    > `INSERT INTO account_warehouse (account_id, warehouse_id) VALUES (1, 3);`
3. Haluan poistaa käyttäjiä. `valmis`
    > `DELETE FROM account_warehouse WHERE account_id = 2;`
    > `DELETE FROM account WHERE id = 2;`
4. Haluan muokata käyttäjän tietoja, kuten nimeä, käyttäjätunnusta tai salasanaa `valmis`
    > `UPDATE account SET name = 'Foo' WHERE id = 1;`
