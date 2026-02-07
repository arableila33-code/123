# Tentamen i Webbramverk

Kom ihåg att varje deluppgift måste lösas i en individuell branch. Om ni inte har separata branches kan ni max uppnå halva poängen per uppgift. Uppgift 1 = en branch. Uppgift 2 = en branch osv.

## Klona projektet

1. Klona projektet med git clone i en mapp och öppna i VSCode.
1. Skapa en virtuell miljö.
1. Aktivera miljön och installera dependencies från requirements.txt.

## Koppla till eget repo

1. Skapa ett repo på github som ni håller privat.
2. Klicka inte i något av fälten som dyker upp. Ni har redan readme, gitignore i detta repo.
3. I terminalen tar ni bort kopplingen till mitt repo:
- git remote remove origin
5. Följ githubs instruktioner för att koppla det klonade repot till er egen github. Oftast något i stil med:
- git remote add origin https://yourlinkhere....
6. Använd sedan GUI eller terminalen för att skapa branches.

Uppskattad tid: 1h för installation och att bekanta sig med koden. Ca 4-5 h för att skriva uppgifterna.

## Uppgifter

**Varje uppgift ska lösas i en egen branch. Kom ihåg att göra commits efter varje uppgift i en ny branch**. Detta är ett måste för att få full pott på uppgifterna. Om ni inte gör detta halveras maxpoängen per uppgift även om ni har 100 % korrekt lösning.
Ingen databas ska installeras utan all data ska skapas i Python med faker eller manuellt.

### Uppgift 1: Flask-grunder (10 p)

1. Skapa app.py med en Flask-applikation.
2. Skapa följande routes:
3. En home branch som visar texten "Välkommen till Flask-övningen!" i ett HTML-element.
4. /about → visar en kort beskrivning av sidan (använd Lorem Ipsum).
5. Applikationen ska köras i debug-läge.

### Uppgift 2: Python-klasser och testdata (10 p)

1. Skapa en Python-klass Product med attribut:
  - i​​​​​​​​d (int)
  - ​​​name (str)
  - pr​​​i​ce (float)
  - cate​g​o​ry (str)
1. Skap​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​a en funktion get_random_products() som returnerar en lista med 5–10 produkter (manuellt eller med Faker).
1. Sk​​​​ap​a en ro​​​ute /products som visar alla produ​​​​​​​​​​​​​kter i en HTML-tabell.
1. Kol​​​​​​​umner: ID, Na​​​​​​​​​me, Pr​​​​​​ice, Cate​​​​gory

### Uppgift 3: Templates och Jinja (10 p)

1. Skapa en base-template base.html som innehåller <head> och <body>-struktur.
2. Skapa en template products.html som ärver från base.html:
3. Rubrik: "Pro​​​​​​​​​​​duktlista"
4. Tabellen från /products ska visas här.
5. Lägg till en navbar i en separat fil _navbar.html med länkar till / och /products.
6. Inkludera navbaren i base-template med {% include '_navbar.html' %}.

### Uppgift 4: Detaljvy och bug-fix (10 p)

1. Skapa en route /product/<int:id> som visar detaljer för en produkt.
2. Visa all information i ett paragraf-element.
3. Om produkten inte finns, returnera "Produkt hittades inte".
4. Skapa en template product_detail_faulty.html med felaktig Jinja som försöker visa en produkt.
5. Fixa templaten så den fungerar korrekt.
6. Lägg till en länk till den i navbaren.

### Uppgift 5: JavaScript-funktioner (10 p)

1. Skapa scripts.js och inkludera den i din HTML så att resultatet syns i webbläsarens konsol.
2. Lös följande uppgifter och logga resultatet med console.log():
3. Funktion sayHello(name) som returnerar "Hej, name" med template-string.
4. Skapa en array prices med siffrorna 10, 20, 30, 40, 50. Lägg till 60 i slutet av arrayen. Logga sedan arrayens längd.
5. Funktion isExpensive(price) som returnerar "Dyr" om pris > 30, annars "Billig".
6. Samma funktion som ovan fast med ternary-operator (? :). Funktionen ska kallas isExpensiveTernary(price).
7. For-loop som skriver ut alla jämna tal mellan två parametrar start och end.
