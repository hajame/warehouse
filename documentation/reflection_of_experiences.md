# Omat kokemukset

## Suunnittelun tavoite

> Aloitin sovelluksen suunnittelun siltä pohjalta, että ehdin saada kaikki perustoiminnallisuudet ajoissa valmiiksi.

Suunnittelu onnistui hyvin. Sovelluksen suunniteltu koko ja ominaisuudet olivat harjoitustyön mittakaavaan sopivat. Tähän vaiheeseen olen erityisen tyytyväinen. 

## Toteutuksen tavoitteet

> Sovelluksen perustoiminnallisuudet ovat kasassa ja niitä on helppo laajentaa.

Elintärkeitä ominaisuuksia ei jätetty toteuttamatta. Sovelluksessa on muutenkin mielestäni melko paljon pinnan alla kytevää toiminnallisuutta.

> Sovellus on jatkuvasti toimivassa tilassa.

Pystyin pushaamaan sovellukseni githubiin toistuvasti toimivassa tilassa, tehden pieniä iteratiivisia muutoksia.

### Onnistumiset

Erityisen mukavaa oli loppusuoralla hyvin onnistuneet ominaisuudet: 

1. varasto-oikeuksian lisääminen käyttäjille, ja käyttäjien tietojen muokkaus
2. esineiden tietojen ja määrän muokkaus siten, ettei varaston kapasiteetti ylity. 
    - Tämä on osin seurausta yhdestä hyvästä päätöksestä tehdä varastoluokalle metodi, joka kertoo voidaanko varastoon lisätä n-määrä tavaraa.
3. Ohjelma on toteutettu siten, että puuttuvat toiminnallisuudet on helppo lisätä jälkikäteen, ja valmiita toiminnallisuuksia on helppo täydentää jälkikäteen. Tämä auttoi monessa tilanteessa, eikä ominaisuuksien lisääminen hirvittänyt yhtä paljon.

### Kömpelyyksiä


1. _Esineen lisääminen ja varaston käyttöoikeuden lisääminen edellyttää, että käyttäjä muistaa varaston nimen kirjain kirjaimelta._ 
    - Tämä ominaisuus korvataan myöhemmin valikolla, jossa on listattuna kaikki sallitut varastot.
2. _Osoiteriviltä pääsee lukemaan ja muokkaamaan mitä tahansa varastoa._ 
    - Myös käyttäjät, joilta muut varastot on piilotettu. Osaavat käyttäjät huomaavat kyllä pian, että osoiteriviltä varasto-id:tä vaihtamalla pääsee pääkäyttäjän tavoin muokkaamaan toisten varastoja.

### Puutteet 

Kuitenkaan kaikkia ei ehditty toteuttaa kuten suunnteltua. Esimerkiksi pääkäyttäjäoikeuden myöntäminen (voi olla, että ehdin lisätä tämän loppurytinän aikana).

### Tunnetut bugit

1. _Esinehaussa listatuista varastoista ensimmäisen varaston "view"-linkki ei toimi._ Yritin korjata tätä ongelmaa todella pitkään siinä onnistumatta. Sain vertaisarvioinnissakin vinkkejä ongelmaan (kiitos tästä __anonOstrich__), mutta valitettavasti en saanut tälläkään ohjeella linkkiä toimimaan.

### Oppiminen

Kurssin aikana opettelin Python-kielen miltei tyhjästä ja opin käyttämään SQL-alchemy-kirjastoa ja monia muita Pythonille tehtyjä web-kirjastoja. Tämän lisäksi opin paljon uutta HTML:stä (kuten formsien käytöstä) sekä open sourcen hyödyllisyydestä, esimerkiksi BootStrap-kirjaston suhteen.

Opin myös hakemaan tietoa ja lukemaan dokumentaatiota paremmin kuin ennen.



