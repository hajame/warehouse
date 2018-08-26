# Käyttötapaukset (user stories)

Alla on kuvattuna varastonhallintasovellukselle olennaisia käyttäjätarinoita.

Käyttäjänä...

1. Haluan tarkastella varastojen sisältöä ja kappalemääriä. [valmis]
    - Näen myös paljonko missäkin varastossa on tilaa jäljellä. [ei toteutettu]
2. Voin lisätä tai poistaa tuotteita varastosta nopeasti. [valmis]
    - Voin kirjoittaa kappalemäärän, joka poistetaan [ei toteutettu]
    - Voin klikata hiirellä yksittäisiä tuotepoistoja tai lisäyksiä [valmis]
    - Voin myös poistaa kaikki samaa nimeä edustavat tuotteet varastosta. [valmis]
3. Haluan luoda uusia varastoja. [valmis]
    - Haluan muokata omien varastojeni tietoja: nimeä ja kapasiteettia. [valmis]
4. Haluan saada tiedon tietyn tuotteen varastotilanteesta. [valmis]
    - Haluan listan varastoista, joissa kyseistä tuotetta on, ja tuotteen kappalemäärät. [valmis, mutta määrät ei näy]
        > `SELECT warehouse.name, warehouse_item.amount FROM account, account_warehouse, warehouse, warehouse_item, item WHERE account.id = account_warehouse.user_id AND account_warehouse.warehouse_id = warehouse.id AND warehouse.id = warehouse_item.warehouse_id AND item.id = warehouse_item.item_id AND item.name = 'Flower pot' ;`
    - Haluan tietää, missä varastossa on eniten kyseistä tuotetta. [ei toteutettu]
        > `SELECT warehouse.name, MAX(WarehouseItem.amount) FROM account, account_warehouse, warehouse, warehouse_item, item WHERE account.id = account_warehouse.user_id AND account_warehouse.warehouse_id = warehouse.id AND warehouse.id = warehouse_item.warehouse_id AND item.id = warehouse_item.item_id AND item.name = 'Flower pot' ;`

Pääkäyttäjänä...

1. Haluan saada listan kaikista järjestelmän varastoista. [valmis]
2. Haluan antaa käyttäjille oikeuksia hallinoida varastoja. [ei toteutettu]
