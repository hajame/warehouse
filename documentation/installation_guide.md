# Sovelluksen asentaminen paikallisesti

*Asennusohjeissa oletetaan, että käyttäjälle on tuttua komentorivin käyttö. Ohjeet on kirjoitettu Linux-käyttöjärjestelmälle*

## Ennakkovaatimukset

Koneessa tulee olla asennettuna 

- python3, jonka mukana tulee pip ja venv
- sqlite3




## Asennus

1. Kloonaa projekti koneellesi

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

8. Navigoi osoitteeseen http://localhost:5000/

9. Voit nyt käyttää sovellusta lokaalissa verkkoympäristössä


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
```
$ cd ~/projekti
$ heroku create projekti
```

5. Viritä seuraavaksi Herokun PostgreSQL tietokanta, jotta sovelluksen tieto tallentuu myös Herokussa
```
$ heroku config:set HEROKU=1
$ heroku addons:add heroku-postgresql:hobby-dev
```

6. Sovelluksella on nyt toimiva PostgreSQL -tietokanta Herokun palvelimella

7. Lisää paikalliseen versionhallintaan tieto Herokusta ja lähetä projekti Herokuun

```
$ git remote add heroku
$ git add .
$ git commit -m "heroku setup"
$ git push heroku master
```

8. Projekti pyörii nyt Herokussa