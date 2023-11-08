import bs4
import requests

resultado = requests.get('https://www.escueladirecta.com/courses')

sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

imagen = sopa.select('.course-box-image')[0]['src']

print(imagen)

imagen_curso_1 = requests.get(imagen)

f = open('mi_imagen.jpg', 'wb')
f.write(imagen_curso_1.content)
f.close()
