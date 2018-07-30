# Käyttötapaukset (user stories)

Alla on kuvattuna varastonhallintasovellukselle olennaisia käyttäjätarinoita.

Käyttäjänä...

1. Haluan tarkastella varastojen sisältöä ja kappalemääriä.
    - Näen myös paljonko missäkin varastossa on tilaa jäljellä.
2. Voin lisätä tai poistaa tuotteita varastosta nopeasti.
    - Voin kirjoittaa poistettavan kappalemäärän tai klikata hiirellä yksittäisiä tuotepoistoja.
    - Voin myös poistaa kaikki saman tyypin tuotteet varastosta.
3. Haluan luoda uusia varastoja ja hallinnoida niiden tietoja.
4. Haluan saada tiedon tietyn tuotteen varastotilanteesta.
    - Haku listaa varastot ja tuotteen kappalemäärät.
    - `SELECT Warehouse.name, WarehouseItem.amount FROM User, WarehouseUser, Warehouse, WarehouseItem, Item WHERE User.id = WarehouseUser.user_id AND WarehouseUser.warehouse_id = Warehouse.id AND Warehouse.id = WarehouseItem.warehouse_id AND Item.id = WarehouseItem.item_id AND Item.name = 'Flower pot' ;`
