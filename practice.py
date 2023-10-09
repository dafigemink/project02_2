import requests

api_key = '6d291603-2b3a-4dff-bb53-d54a0e7cb791'
word = 'apple'
url = f'https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={api_key}'

res = requests.get(url)

definitions = res.json()

for definition in definitions:
    print(definition)