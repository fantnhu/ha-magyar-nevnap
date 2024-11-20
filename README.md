# Magyar Névnap Integráció a Home Assistant-hoz
## Áttekintés
Ez egy custom integráció, amely a magyar névnapokat jeleníti meg a Home Assistant rendszerben. Az integráció két szenzort hoz létre:
-	Névnap elsődleges
-	Névnap másodlagos

Ha az adott napon két névnap van, ezek az entitások a névnapokat jelenítik meg. Az integráció elsősorban magyar felhasználóknak készült, mivel magyar neveket tartalmaz, és Magyarországon ünnepeljük a névnapokat.
________________________________________
## Fő jellemzők
-	Két szenzor a névnapok megjelenítésére.
-	Könnyen telepíthető a HACS-on keresztül vagy manuálisan.
-	Felhasználói felületen keresztül konfigurálható.
________________________________________
## Telepítés
### 1. Telepítés HACS-on keresztül
1.	Győződj meg róla, hogy a Home Assistant Community Store (HACS) telepítve van.
2.	Nyisd meg a HACS-t a Home Assistant rendszerben.
3.	Válaszd a Integrations szekciót.
4.	Kattints a jobb felső sarokban lévő "+" gombra.
5.	Keresd meg a **Magyar Névnap** Integráció-t.
6.	Kattints a Download (Letöltés) gombra.
7.	Indítsd újra a Home Assistant rendszert.
________________________________________
### 2. Manuális telepítés
1.	Töltsd le az integráció legfrissebb verzióját a GitHub repóból.
2.	Csomagold ki a letöltött fájlokat.
3.	Másold a kicsomagolt mappát a Home Assistant rendszer custom_components mappájába. Például: * */config/custom_components/magyar_nevnap* *
4.	Indítsd újra a Home Assistant rendszert.
________________________________________
## Konfiguráció
Az integráció konfigurálható a Home Assistant felhasználói felületén:
1.	Navigálj a **Beállítások** > **Eszközök** és szolgáltatások menübe.
2.	Kattints az **Integráció hozzáadása** gombra.
3.	Keresd meg a **Magyar Névnap Integráció**-t a listában.
4.	Kövesd a megjelenő utasításokat.
________________________________________
## Miért magyaroknak?
-	A névnapok hagyománya Magyarországra jellemző.
-	Az integráció kizárólag magyar neveket tartalmaz.
-	Magyar nyelvű megjelenítést biztosít.
________________________________________
## Hibajelentés és fejlesztési ötletek
Ha hibát találsz vagy javaslatod van, nyiss egy [issue-t a GitHub oldalon](https://github.com/fantnhu/ha-magyar-nevnap/issues/).
________________________________________
## Képernyőképek
Példa szenzor értékek:
-	Névnap elsődleges: "István"
-	Névnap másodlagos: "János"
________________________________________
## Licenc
Ez a projekt az MIT Licenc alatt érhető el.

