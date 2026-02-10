# Tentamen i Webbramverk

Kom ihåg att varje deluppgift måste lösas i en individuell branch. Om ni inte har separata branches kan ni max uppnå halva poängen per uppgift. Uppgift 1 = en branch. Uppgift 2 = en branch osv.

## Klona projektet

1. Klona projektet med git clone i en mapp och öppna i VSCode.
1. Skapa en virtuell miljö.
1. Aktivera miljön och installera dependencies från requirements.txt.

## Koppla till eget repo

1. Skapa ett repo på github som ni håller privat.
1. Ni har redan .gitignore och readme i detta repo. Klicka endast i att repot ska hållas Privat och lämna resten tomma.
1. I terminalen i VSCode tar ni bort kopplingen till mitt repo:
    - git remote remove origin
1. Följ githubs instruktioner för att koppla det klonade repot till er egen github. Oftast något i stil med:
    - git remote add origin your-GitHub-link-here
1. Använd git remote -v i terminalen för att kontrollera kopplingen. Er remote-länk bör dyka upp här innan ni fortsätter med tentamen.
1. Använd sedan GUI eller terminalen för att skapa branches.

Uppskattad tid: 1h för installation och att bekanta sig med koden. Ca 4-5 h för att skriva uppgifterna.

## Uppgifter

**Varje uppgift ska lösas i en egen branch. Kom ihåg att göra commits efter varje uppgift i en ny branch. Att skapa branches och göra commits är inkluderat i skrivtiden.**. Detta är ett måste för att få full pott på uppgifterna. Om ni inte gör detta halveras maxpoängen per uppgift även om ni har 100 % korrekt lösning.
Ingen databas ska installeras utan all data ska skapas i Python med faker eller manuellt.
Styling är inget examinerande moment och ni behöver inte skriva eller länka till någon css alls.

### Uppgift 1: Flask-grunder (10 p)

1. Skapa app.py med en Flask-applikation.
2. Applikationen ska köras i debug-läge.
3. Skapa följande routes:
    - En home branch som visar texten "Välkommen till min sluttentamen" i ett lämpligt HTML-element. Bilden som finns i static-mappen ska även länkas på hemsidan.
    - En about us som visar en kort beskrivning av sidan. Använd Lorem Ipsum eller kopiera in text från någon nyhetsartikel eller liknande. Använd ett lämpligt HTML-element för detta.

### Uppgift 2: Python-klasser och testdata (10 p)

1. Skapa en Python-klass Product med följande attribut:
    - i​​​​​​​​d
    - ​​​name
    - pr​​​i​ce
    - cate​g​o​ry
    - ingredients
1. Skap​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​a en funktion get_random_products() som returnerar en lista med 5–10 produkter (manuellt eller med Faker).
1. Sk​​​​ap​a en ro​​​ute som visar alla produ​​​​​​​​​​​​​kter i en HTML-tabell. Tabellen ska innehålla kolumnerna från klassen ni skapade. Templaten ni skriver här ska endast innehålla en HTML-tabell. Ingen <head>-tagg eller liknande.

### Uppgift 3: Templates och Jinja (10 p)

1. Skapa en bas-template som innehåller standard HTML-struktur (!+tab i VSCode). Lägg till er själva som author i relevant tagg.
2. Tabellen från föregående uppgift ska visas här. Ni ska alltså se till att tabellen från föregående uppgift på något sätt hamnar i er bas-template.
3. Lägg till en navbar i en separat fil _navbar.html med länkar till era routes.
4. Inkludera navbaren i er bas-template.

### Uppgift 4: Detaljvy och bug-fix (10 p)

1. I koden finns det en blueprint som ska visa detaljerna för en specifik produkt men den innehåller dessvärre buggar.
2. Av någon anledning så går det inte att nå vår blueprint och ni måste registrera denna.
3. Lägg till en länk till denna route i er navbar.
4. Templaten som finns länkad innehåller ett antal fel som ni måste rätta till. Målet är att vi ska kunna se produktens attribut som text på skärmen.
5. Om produkten inte finns, returnera "Produkt hittades inte".

### Uppgift 5: JavaScript-funktioner (10 p)

1. Skapa en script-fil och inkludera den i din HTML så att resultatet går att se i webbläsarens konsol. Använd strict mode i er fil.
2. Lös följande uppgifter och logga resultaten med console.log():
3. Funktion sayHello(name) som returnerar "Hej, name" med template-string.
4. Skapa en array prices med siffrorna 10, 20, 30, 40, 50. Lägg till 60 i slutet av arrayen. Logga sedan arrayens längd.
5. Funktion isExpensive(price) som returnerar "Dyr" om pris > 30, annars "Billig".
6. Samma funktion som ovan fast med ternary-operator (? :). Funktionen ska kallas isExpensiveTernary(price).
7. For-loop som skriver ut alla jämna tal mellan två parametrar start och end.
