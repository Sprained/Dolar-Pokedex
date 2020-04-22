import requests
import json

req = requests.get('https://economia.awesomeapi.com.br/all/USD-BRL')

cotacao = req.json()
print('Dolar: ' + cotacao['USD']['bid'])
cotacaoFloat = round(float(cotacao['USD']['bid']), 2)
cotacaoString = str(cotacaoFloat).replace('.', '')

poke = requests.get('https://pokeapi.co/api/v2/pokemon/' + cotacaoString)
pokedex = poke.json()
print('O seu dolar pokemon é ' + pokedex['forms'][0]['name'])