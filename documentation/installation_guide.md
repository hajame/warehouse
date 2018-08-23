# Sovelluksen asentaminen paikallisesti

*Asennusohjeissa oletetaan, että käyttäjälle on tuttua komentorivin käyttö. Ohjeet on kirjoitettu Linux-käyttöjärjestelmälle*

## Ennakkovaatimukset

Koneessa tulee olla asennettuna 

- python3, jonka mukana tulee pip ja venv
- sqlite3




## Asennus

1. Kloonaa projekti koneellesi haluamaasi kansioon.

```
$ git clone git@github.com:hajame/warehouse.git
```

Voit myös ladata osoitteesta https://github.com/hajame/warehouse projektin .ZIP-tiedostona ja purkaa sen.

2. Luo Pythonin virtuaaliympäristö ja ota se käyttöön seuraavilla komennoilla
```
$ python3 -m venv venv
$ source venv/bin/activate
```

3. Asenna sovelluksen requirements.txt määrittelemät riippuvuudet

```
$ pip install -r requirements.txt
```

7. Voit nyt käyttää sovellusta käynnistämällä sen seuraavalla komennolla
```
$ python3 run.py
```


8. Lisää sovellukseen ensimmäinen pääkäyttäjä

Kirjoita seuraavat komennot terminaaliin. Vaihda kenttien nimi, käyttäjätunnus ja salasana haluamiksisi.

_HUOM!_ role_id:n tulee olla 2, jotta käyttäjällä on pääkäyttäjän oikeudet

```
$ sqlite3 application/warehouses.db 
sqlite> INSERT INTO account (name, username, password, role_id) VALUES ('Admin', 'admin', 'pass', 2);
```

9. Navigoi osoitteeseen http://localhost:5000/

10. Voit nyt käyttää sovellusta lokaalissa verkkoympäristössä


## Sovelluksen asentaminen Herokuun

+ requirements.txt:n ja koodissa olevien määrittelyiden pitäisi olla ajantasalla automaattisesti, jos projekti on kopioitu githubista.

1. Asenna sovellus yllä kuvatun mukaisesti paikallisesti

2. Asenna koneellesi Herokun komentorivisovellus

Linux:
```
$ sudo snap install heroku --classic
```
MacOS:
```
$ brew install heroku/brew/heroku
```

3. Kirjaudu sisään Herokuun

```
$ heroku login
```

4. Navigoi kansioon johon loit paikallisen projektin ja luo Heroku projekti siitä

Vaihda saman _projekti_ haluamasi projektin nimi.
```
$ cd ~/projekti
$ heroku create projekti
```

5. Lisää paikalliseen versionhallintaan tieto Herokusta ja lähetä projekti Herokuun

```
$ git remote add heroku
$ git add .
$ git commit -m "heroku setup"
$ git push heroku master
```

6. Projekti pyörii nyt Herokussa

7. Viritä seuraavaksi Herokun PostgreSQL tietokanta, jotta sovelluksen tieto tallentuu myös Herokussa
```
$ heroku config:set HEROKU=1
$ heroku addons:add heroku-postgresql:hobby-dev
```

8. Sovelluksella on nyt toimiva PostgreSQL -tietokanta Herokun palvelimella

9. Lisää sovellukseen ensimmäinen pääkäyttäjä

Kirjoita komentoriville. Vaihda kenttien nimi, käyttäjätunnus ja salasana haluamiksisi.

_HUOM!_ role_id:n tulee olla 2, jotta käyttäjällä on pääkäyttäjän oikeudet

```
$ heroku pg:psql
projekti::DATABASE=> INSERT INTO account (name, username, password, role_id) VALUES ('Admin', 'admin', 'pass', 2);
```

