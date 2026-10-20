![](https://raw.githubusercontent.com/fantnhu/ha-magyar-nevnap/refs/heads/main/img/header_img.png)
# Magyar Névnap Integráció Home Assistant-hoz

***This integration might be interesting for Hungarian users! This integration collects the Hungarian name days.***

## 📝 Leírás

A Magyar Névnap integráció lehetővé teszi a magyar névnapok megjelenítését a Home Assistant rendszerben. Az integráció elsősorban magyar felhasználóknak készült, mivel magyar neveket tartalmaz, és Magyarországon ünnepeljük a névnapokat.

## ✨ Funkciók

- 🎯 **Kiemelt névnap**: Az aktuális nap fő névnapjai
- 📅 **Másodlagos névnap**: Az aktuális nap további névnapjai
- 📆 **Naptár entitás**: A mai névnapok egész napos eseményként jelennek meg
- 💝 **Névfigyelő**: Megadhatod, mely neveket szeretnéd figyelni, és automatizálást készíthetsz a találatokhoz
- 🔄 **Kézi frissítés**: Egy gombnyomással lekérheted az aktuális adatokat
- ⚙️ **Állítható frissítés**: Te választhatod meg a lekérések gyakoriságát
- 🌷 **Saját ikon**: Tulipános naptárikon világos és sötét témához

## 🛠️ Telepítés

A használathoz Home Assistant 2026.3 vagy újabb szükséges.

1. Másold a `custom_components/magyar_nevnap` mappát a Home Assistant `custom_components` könyvtárába
2. Indítsd újra a Home Assistant-ot
3. Menj a Beállítások > Eszközök és szolgáltatások menüpontba
4. Kattints az "Integráció hozzáadása" gombra
5. Keresd meg a "Magyar Névnap" integrációt
6. Kövesd a telepítési varázsló lépéseit

Ha már használod az integrációt, elég felülírnod a fájljait és újraindítanod a Home Assistantot. Az integrációt nem kell törölni és újra hozzáadni: a meglévő szenzorok és a naptár azonosítói megmaradnak.

## 📊 Entitások

### Szenzorok

| Entitás | Típus | Leírás |
|---------|-------|--------|
| `sensor.magyar_nevnap_kiemelt_nevnap` | `string` | Az aktuális napra eső névnap |
| `sensor.magyar_nevnap_masodlagos_nevnap` | `string` | Az aktuális nap további névnapjai |

A szenzorok `names` attribútumában listaként is elérhetők a nevek. A `full_text` tartalmazza a teljes szöveget akkor is, ha az állapot a Home Assistant hosszkorlátja miatt rövidül.

Az **Utolsó sikeres frissítés** diagnosztikai szenzor megmutatja, mikor érkezett utoljára érvényes válasz. Alapból ki van kapcsolva; az integráció entitáslistájában engedélyezheted.

### Naptár

| Entitás | Típus | Leírás |
|---------|-------|--------|
| `calendar.magyar_nevnap_magyar_nevnap` | `calendar` | A mai névnap egész napos eseményként |

A további nevek az esemény leírásában szerepelnek. A naptár a mai napot mutatja, jövőbeli névnapokat egyelőre nem tartalmaz. A szenzorok átnevezése nem befolyásolja a működését.

### Névfigyelő és frissítőgomb

A **Figyelt névnap ma** bináris szenzor akkor jelenik meg, ha megadsz legalább egy figyelt nevet. Találat esetén bekapcsol, a megfelelő neveket a `matched_names` attribútumban találod.

A **Frissítés** gomb az integráció eszközoldalán érhető el.

Az entitásazonosítók a Home Assistant nyelvétől és a korábbi átnevezésektől függően eltérhetnek a példáktól.

## ⚙️ Konfiguráció

Az integráció külön beállítás nélkül is működik. A **Beállítások > Eszközök és szolgáltatások > Magyar Névnap > Beállítások** alatt ezeket módosíthatod:

| Beállítás | Alapérték | Mire szolgál? |
|-----------|-----------|--------------|
| Frissítési időköz | 60 perc | 5 és 1440 perc között állítható |
| Figyelt nevek | Üres | Vesszővel elválasztott nevek, például `Anna, István` |
| Másodlagos névnapok figyelése is | Bekapcsolva | A névfigyelő a további nevek között is keres |

A névfigyelő nem tesz különbséget kis- és nagybetűk között, de az ékezetek számítanak. Az `Anna` és a `Marianna` külön névnek számít. A névlista a Home Assistantban marad, az API nem kapja meg.

Értesítést vagy hangos köszöntést saját automatizálással készíthetsz. Napi köszöntéshez érdemes egy megadott időpontban ellenőrizni a névfigyelőt, mert két egymást követő találatos napon nem feltétlenül vált újra kikapcsoltról bekapcsoltra.

## 🔄 Frissítési gyakoriság

- Alapból óránként frissülnek az adatok, és a Home Assistant helyi ideje szerint éjfélkor is történik lekérés.
- A szenzorok és a naptár közös adatlekérést használnak.
- Ha a szolgáltatás nem érhető el vagy hibás választ ad, az entitások elérhetetlennek látszanak. A következő sikeres frissítéskor maguktól helyreállnak.

## 🎨 Testreszabás

Az integráció saját tulipános ikont kapott. A névnapszenzorok alapértelmezett ikonja továbbra is `mdi:party-popper`; ezt az entitás beállításainál szabadon módosíthatod.

## 📋 Változások

Az újdonságokat és javításokat a [változásnaplóban](CHANGELOG.md) találod.

## 🤝 Közreműködés

Ha hibát találsz vagy fejlesztési javaslatod van, kérlek nyiss egy [issue-t a GitHub oldalon](https://github.com/fantnhu/ha-magyar-nevnap/issues/)

## 📄 Licensz

Ez a projekt MIT licensz alatt áll.

## 🔗 Hasznos linkek

- [Home Assistant közösség](https://community.home-assistant.io/)

