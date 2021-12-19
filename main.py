
import requests

#задача1

hero1 = 'Hulk'
hero2 = 'Captain America'
hero3 = 'Thanos'

def get_intelligence(name):
    URL = 'https://superheroapi.com/api/2619421814940190/' + 'search/' + name

    response = requests.get(URL)
    json_ = response.json()

    if json_['response'] != 'error':
        return int((json_['results'][0]['powerstats']['intelligence']))
    else:
        return 0

result = {}
result[hero1] = get_intelligence(hero1)
result[hero2] = get_intelligence(hero2)
result[hero3] = get_intelligence(hero3)

max_intelligence = 0
max_intelligence_name  = ''
for key, value in result.items():
    if value > max_intelligence:
        max_intelligence = value
        max_intelligence_name = key

print('Cамый сильный герой: ',max_intelligence_name,'\n','Сила: ', max_intelligence)

