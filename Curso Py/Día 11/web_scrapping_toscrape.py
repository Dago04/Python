import bs4
import requests


url_base = 'http://books.toscrape.com/catalogue/page-{}.html'

titulos_rating_alto = []

for pagina in range(1, 51):
    url_pagina = url_base.format(pagina)
    resul = requests.get(url_pagina)
    sopa = bs4.BeautifulSoup(resul.text, 'lxml')


libros = sopa.select('.product_pod')

ejemplo = libros[0].select('a')[1]['title']
