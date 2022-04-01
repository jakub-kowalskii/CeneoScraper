# CeneoScraper

## Struktura opinii w serwisie [ceneo.pl](https://www.ceneo.pl/101052360#tab=reviews)

|Składowa opinii|Selektor|Nazwa zmiennej|Typ danych|
|---------------|--------|--------------|----------|
|Opinia|div.js_product-review|||
|Identyfikator opinii|div.js_product-review\["data-entry-id"\]|||
|Autor opinii|span.user-post__author-name|||
|rekomendacja autora|span.user-post_author-recommendation > em|||
|liczba gwiazdek|span.user-post__score-count|||
|treść opinii|div.user-post__text|||
|lista zalet|review-feature_col:nth-child(1)|||
|lista wad|review-feature_col:nth-child(2)|||
|dla ilu osób przydatna|button.vote-yes > span|||
|dla ilu osób nieprzydatna|button.vote-no > span|||
|data wystawienia opinii|span.user-post__published > time:nth-child(1)\["datetime"\]|||
|data zakupu produktu|.user-post__published > time:nth-child(2)\["datetime"\]|||