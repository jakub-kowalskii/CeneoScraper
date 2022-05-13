# CeneoScraper

## Struktura opinii w serwisie [ceneo.pl](https://www.ceneo.pl/101052360#tab=reviews)

|Składowa opinii|Selektor|Nazwa zmiennej|Typ danych|
|---------------|--------|--------------|----------|
|Opinia|div.js_product-review|opinion|bs4.element.Tag|
|Identyfikator opinii|div.js_product-review\["data-entry-id"\]|opinion_id||
|Autor opinii|span.user-post__author-name|author||
|rekomendacja autora|span.user-post_author-recommendation > em|recommendation||
|liczba gwiazdek|span.user-post__score-count|stars||
|treść opinii|div.user-post__text|content||
|lista zalet|div[class$=positives] ~ div.review-feature__item|pros||
|lista wad|div[class$=negatives] ~ div.review-feature__item|cons||
|dla ilu osób przydatna|button.vote-yes > span|useful||
|dla ilu osób nieprzydatna|button.vote-no > span|useless||
|data wystawienia opinii|span.user-post__published > time:nth-child(1)\["datetime"\]|published||
|data zakupu produktu|.user-post__published > time:nth-child(2)\["datetime"\]|purchased||

## Etapy pracy nad projektem strukturalnym
1. Pobranie elementów pojedynczej opinii do niezależnych zmiennych
2. Zapisanie wszystkich elementów pojedynczej opinii jednej zmiennej \(słownik\)
3. Pobranie wszystkich opinii z pojedynczej strony do słowników i dodanie ich do listy
4. Pobranie wszystkich opinii o produkcie z wszystkich stron i zapisanie ich do pliku .json
5. Dodanie możliwości wpisania id produktu przez użytkownika za pomocą klawiatury
6. Refaktoryzacja \(optymalizacja\) kodu:
    a. utworzenie funkcji do pobierania składowych strony HTML
    b. utworzenie słownika opisującego strukturę opinii wraz z selektorami poszczególnych elementów
    c. zamiana instrukcji pobierających składowe opinii do pojedynczych zmiennych i tworzących z nich słownik na wyrażenie słownikowe \(dictionary comprehension\) tworzące słownik reprezentujący pojedynczą opinię na podstawie słownika selektorów
7.Analiza opinii o danym produkcie
    1.Wczytywanie wszystkich opinii o produkcie do obiektu DataFrame
    2.Wyliczanie podstawowych statystyk na podstawie opinii
        1.liczba wszystkich opinii o produkcie
        2.liczba opinii w których autor podał zalety
        3.listę opinii w których autor podał wady
        4.średnia oceny produktu
    3.Przygotowanie wykresu na podstawie opinii
        1. Udział poszczególnych rekomendacji w ogólnej liczbie opinii
        2. histogram częstości występowania poszczególnych ocen