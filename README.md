Remember to add me as a collaborator after handing in the exam!
Kom ihåg att bjuda in mig som collaborator efter att ni skickat in tentamen!

English version further down

# Tentamen i Webbramverk

Kom ihåg att varje deluppgift måste lösas i en individuell branch. Om ni inte har separata branches kan ni max uppnå halva poängen per uppgift. Uppgift 1 = en branch. Uppgift 2 = en branch osv.
Det viktiga är att ni jobbar i olika branches och jag kommer att kolla er historik på hur ni har löst uppgifterna. Om ni inte har perfekt historik mellan era branches är det helt ok. Ni behöver inte göra en merge till main mellan varje branch utan det räcker med att pusha upp era branches till github.

Styling med css är inte en examinerande del. Ni behöver alltså inte lägga ner någon tid på att ändra färger eller utseende.

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

### Uppgift 1: Flask-grunder (9 p)

1. Skapa app.py med en Flask-applikation.
2. Applikationen ska köras i debug-läge.
3. Skapa följande routes i app.py som skickar tillbaka html-templates:
    - En home route som visar texten "Välkommen till min sluttentamen" i ett lämpligt HTML-element. Bilden som finns i static-mappen ska även länkas på startsidan (home). Ingen styling behövs.
    - En about us-template som visar en kort beskrivning av sidan. Denna ska vara separerad från home. Använd Lorem Ipsum eller kopiera in text från någon nyhetsartikel eller liknande. Använd ett lämpligt HTML-element för denna text.

---

### Uppgift 2: Python-klasser och testdata (9 p)

1. Skapa en Python-klass Product med följande attribut:
    - i​​​​​​​​d
    - ​​​name
    - pr​​​i​ce
    - cate​g​o​ry
    - ingredients
1. Skap​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​a en funktion get_random_products() inuti samma fil som klassen som returnerar en lista med 5–10 produkter (manuellt eller med Faker).
1. Sk​​​​ap​a en ro​​​ute som visar alla produ​​​​​​​​​​​​​kter i en HTML-tabell. Tabellen ska innehålla kolumnerna från klassen ni skapade. Templaten ni skriver här ska endast innehålla en HTML-tabell och ska endast innehålla produkt-datan. Alltså inget arv från en bas-template på denna uppgift.

---

### Uppgift 3: Templates och Jinja (12 p)

1. Skapa en bas-template som innehåller standard HTML-struktur (!+tab i VSCode). Lägg till er själva med ert namn som author i relevant tagg.
2. Tabellen från föregående uppgift ska nu ärva denna bas-template.
3. Lägg till en navbar i en separat fil _navbar.html med länkar till era routes.
4. Inkludera navbaren i er bas-template och se till att det går att nå de olika länkarna:
    - Home
    - About Us
    - Products (=er tabell)

---

### Uppgift 4: Detaljvy och bug-fix (12 p)

1. I koden finns det en blueprint med en route som ska visa detaljerna för en specifik produkt men den innehåller dessvärre buggar. Av någon anledning så går det inte att nå vår blueprint och ni måste registrera denna.
2. Lägg till en länk till denna route i er tabell som ett extra fält.
3. Templaten som finns länkad innehåller ett antal fel som ni måste rätta till. Målet är att vi ska kunna se produktens attribut som text på skärmen.
4. Om produkten inte finns, visa "Produkt hittades inte" på sidan som text.

---

### Uppgift 5: JavaScript-funktioner (14 p)

1. Skapa en script-fil och inkludera den i din HTML så att resultatet går att se i webbläsarens konsol. Använd strict mode i er fil.
2. Lös följande uppgifter och logga resultaten med console.log():
3. Funktion sayHello(name) som returnerar "Hej, name" med template-string.
4. Skapa en array prices med siffrorna 10, 20, 30, 40, 50. Lägg till 60 i slutet av arrayen. Logga sedan arrayens längd.
5. Funktion isExpensive(price) som returnerar "Dyr" om pris > 30, annars "Billig".
6. Samma funktion som ovan fast med ternary-operator (? :). Funktionen ska kallas isExpensiveTernary(price).
7. For-loop som skriver ut alla jämna tal mellan två parametrar start och end.

---

English intructions
# Exam in Flask

Remember that each subtask must be completed in an individual branch. If you do not have separate branches, you can achieve at most half the points per task. Task 1 = one branch. Task 2 = one branch, etc.
The important thing is that you work in different branches, and I will check your history to see how you solved the tasks. If your history between branches is not perfect, that is completely fine. You do not need to merge to main between each branch; it is enough to push your branches to GitHub.

Styling with CSS is not part of the assessment. You do not need to spend any time changing colors or appearance.

## Clone the Project

1. Clone the project using `git clone` into a folder and open it in VSCode.
2. Create a virtual environment.
3. Activate the environment and install dependencies from `requirements.txt`.

## Connect to Your Own Repository

1. Create a repository on GitHub and keep it private.
2. You already have a `.gitignore` and `README` in this repository. Only check that the repository should be private and leave the rest empty.
3. In the VSCode terminal, remove the connection to my repository:
   * `git remote remove origin`
4. Follow GitHub’s instructions to connect the cloned repository to your own GitHub. Usually something like:
   * `git remote add origin your-GitHub-link-here`
5. Use `git remote -v` in the terminal to verify the connection. Your remote link should appear here before you continue with the exam.
6. Then use the GUI or terminal to create branches.

Estimated time: 1 hour for installation and getting familiar with the code. About 4–5 hours to complete the tasks.

## Tasks

**Each task must be completed in its own branch. Remember to make commits after each task in a new branch. Creating branches and making commits is included in the writing time.** This is mandatory to receive full points for the tasks. If you do not do this, the maximum score per task will be halved even if you have a 100% correct solution.

No database should be installed; all data must be created in Python using Faker or manually.
Styling is not part of the assessment, and you do not need to write or link any CSS at all.

---

## Task 1: Flask Basics (9 points)

1. Create `app.py` with a Flask application.
2. The application should run in debug mode.
3. Create the following routes in `app.py` that return HTML templates:
   * A home route that displays the text “Welcome to my final exam” in an appropriate HTML element. The image located in the `static` folder should also be linked on the home page. No styling is needed.
   * An about us template that displays a short description of the page. This should be separate from home. Use Lorem Ipsum or copy text from a news article or similar. Use an appropriate HTML element for this text.

---

## Task 2: Python Classes and Test Data (9 points)

1. Create a Python class `Product` with the following attributes:
   * id
   * name
   * price
   * category
   * ingredients
2. Create a function `get_random_products()` in the same file as the class that returns a list of 5–10 products (manually or using Faker).
3. Create a route that displays all products in an HTML table. The table should contain the columns from the class you created. The template written here should only contain an HTML table and only include the product data. Do not inherit from a base template in this task.

---

## Task 3: Templates and Jinja (12 points)

1. Create a base template that contains a standard HTML structure (`! + tab` in VSCode). Add yourself with your name as the author in the relevant tag.
2. The table from the previous task should now inherit from this base template.
3. Add a navbar in a separate file `_navbar.html` with links to your routes.
4. Include the navbar in your base template and make sure the following links are accessible:

   * Home
   * About Us
   * Products (= your table)

---

## Task 4: Detail View and Bug Fix (12 points)

1. In the code, there is a blueprint with a route that should display the details of a specific product, but it unfortunately contains bugs. For some reason, the blueprint cannot be reached, and you must register it.
2. Add a link to this route in your table as an extra field.
3. The linked template contains several errors that you must fix. The goal is to display the product’s attributes as text on the screen.
4. If the product does not exist, display “Product not found” as text on the page.

---

## Task 5: JavaScript Functions (14 points)

1. Create a script file and include it in your HTML so that the result can be seen in the browser console. Use strict mode in your file.
2. Solve the following tasks and log the results using `console.log()`:
3. Function `sayHello(name)` that returns “Hello, name” using a template string.
4. Create an array `prices` with the numbers 10, 20, 30, 40, 50. Add 60 to the end of the array. Then log the length of the array.
5. Function `isExpensive(price)` that returns “Expensive” if price > 30, otherwise “Cheap”.
6. The same function as above but using a ternary operator (`? :`). The function should be called `isExpensiveTernary(price)`.
7. A for-loop that prints all even numbers between two parameters `start` and `end`.
