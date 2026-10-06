# 📋 Változások

## 1.1.1

- A használati útmutató kiegészült a névfigyelő beállításaival, az új entitásokkal és a frissítés menetével.
- Kódtisztítás, működésbeli változás nélkül.

## 1.1.0

### Újdonságok

- Névfigyelő a beállított nevekhez, a másodlagos névnapok választható figyelembevételével.
- A frissítési időköz 5 és 1440 perc között állítható.
- Kézi frissítőgomb és külön engedélyezhető szenzor az utolsó sikeres frissítéshez.
- A névlisták a szenzorok attribútumaiban is elérhetők, teljes szövegként és listaként.
- Magyar és angol felületi szövegek, saját tulipános integrációikon.

### Javítások

- A naptár egész napos eseményt ad vissza, a következő nap kezdetéig. A szenzor átnevezése többé nem szakítja meg a naptár működését.
- A szenzorok és a naptár egyetlen közös API-lekérést használnak.
- A hiányos vagy hibás API-válasz nem írja felül üres szöveggel a névnapokat. Az entitások ilyenkor elérhetetlenséget jeleznek, majd a következő sikeres lekéréskor helyreállnak.
- A hosszú névlisták nem lépik túl a szenzorállapot 255 karakteres korlátját; a teljes szöveg attribútumban megmarad.

A meglévő szenzorok és a naptár egyedi azonosítói változatlanok.

## 1.0.0

- Kiemelt és másodlagos névnapok megjelenítése szenzorokkal.
- Naptár entitás a mai névnaphoz.
- Óránkénti automatikus frissítés.
