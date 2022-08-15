#importando as bibliotecas necessárias
import quotes as quotes
from bs4 import BeautifulSoup
import html5lib
import requests
import csv

 #Link do site que iremos utilizar
url = 'https://www.brainyquote.com/topics/motivational-quotes'
r = requests.get(url)
print(r.content)

soup = BeautifulSoup(r.content, 'html5lib') #r.content é a string que será usada e o html5 vai atuar com o html do site indicado

table= soup.find('div', attrs={'id':'quotesList'})
print(table.prettify())

for row in table.findAll('div',attrs={'class':'qtd-listm'}): #buscando por todas as divs com class e qtd-listm
    quote = {}
    try:
        quote['author'] = row.img['alt'].split("-")[1] #informando o autor
        quote['text'] = row.img['alt'].split("-")[0]   #mostrando a frase do autor
        quotes.append(quote)

    except TypeError:
        continue

