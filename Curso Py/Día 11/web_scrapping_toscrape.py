import bs4
import requests


url_base = 'http://books.toscrape.com/catalogue/page-{}.html'

titulos_rating_alto = []

for pagina in range(1, 51):
    url_pagina = url_base.format(pagina)
    resul = requests.get(url_pagina)
    sopa = bs4.BeautifulSoup(resul.text, 'lxml')

    libros = sopa.select('.product_pod')

    for libro in libros:
        if len(libro.select('.star-rating-Four')) != 0 or len(libro.select('.star-rating-Five')):

            titulo_libro = libro.select('a')[1]['title']

            titulos_rating_alto.append(titulo_libro)


for t in titulos_rating_alto:
    print(t)
