import requests
import json

req = requests.get('https://economia.awesomeapi.com.br/all/USD-BRL')

cotacao = req.json()
print('Dolar: ' + cotacao['USD']['bid'])
cotacaoString = str(cotacao['USD']['bid'])
cotacaoString = cotacaoString.replace('.', '')

poke = requests.get('https://pokeapi.co/api/v2/pokemon/' + cotacaoString[:-2])
pokedex = poke.json()
print('O seu dolar pokemon é ' + pokedex['forms'][0]['name'])