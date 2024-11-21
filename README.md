![](https://raw.githubusercontent.com/fantnhu/ha-magyar-nevnap/refs/heads/main/img/header_img.png)
# Magyar Névnap Integráció Home Assistant-hoz

***This integration might be interesting for Hungarian users! This integration collects the Hungarian name days.***

## 📝 Leírás

A Magyar Névnap integráció lehetővé teszi a magyar névnapok megjelenítését a Home Assistant rendszerben. Az integráció elsősorban magyar felhasználóknak készült, mivel magyar neveket tartalmaz, és Magyarországon ünnepeljük a névnapokat.

## ✨ Funkciók

- 🎯 **Kiemelt névnap**: Az aktuális nap első névnapja
- 📅 **Másodlagos névnap**: Az aktuális nap további névnapjai
- 📆 **Naptár entitás**: A névnapok naptár formátumban is elérhetők

## 🛠️ Telepítés

1. Másold a `custom_components/magyar_nevnap` mappát a Home Assistant `custom_components` könyvtárába
2. Indítsd újra a Home Assistant-ot
3. Menj a Beállítások > Eszközök és szolgáltatások menüpontba
4. Kattints az "Integráció hozzáadása" gombra
5. Keresd meg a "Magyar Névnapok" integrációt
6. Kövesd a telepítési varázsló lépéseit

## 📊 Entitások

### Szenzorok

| Entitás | Típus | Leírás |
|---------|-------|--------|
| `sensor.magyar_nevnap_kiemelt_nevnap` | `string` | Az aktuális napra eső névnap |
| `sensor.magyar_nevnap_masodlagos_nevnap` | `string` | Az aktuális nap további névnapjai |

### Naptár

| Entitás | Típus | Leírás |
|---------|-------|--------|
| `calendar.magyar_nevnapok` | `calendar` | A névnapok naptár formátumban |

## ⚙️ Konfiguráció

Az integráció nem igényel további konfigurációt a telepítés után. Az adatok automatikusan frissülnek óránként.

## 🔄 Frissítési gyakoriság

- A frissítési intervallum: 1 óra

## 🎨 Testreszabás

Az entitások alapértelmezett ikonja: `mdi:party-popper`

## 🤝 Közreműködés

Ha hibát találsz vagy fejlesztési javaslatod van, kérlek nyiss egy [issue-t a GitHub oldalon](https://github.com/fantnhu/ha-magyar-nevnap/issues/)

## 📄 Licensz

Ez a projekt MIT licensz alatt áll. További információért lásd a LICENSE fájlt.

## 🔗 Hasznos linkek

- [Home Assistant közösség](https://community.home-assistant.io/)

