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
max_intelligence_name = ''
for key, value in result.items():
    if value > max_intelligence:
        max_intelligence = value
        max_intelligence_name = key

print('Cамый сильный герой: ', max_intelligence_name, '\n', 'Сила: ', max_intelligence)

#Задача2

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        url = f'https://cloud-api.yandex.net/v1/disk/resources/upload?path={file_path}&overwrite=true'

        headers = {'Authorization': token,
                   'Accept': 'application/json'}

        session = requests.Session()
        request = session.get(url, headers=headers)

        href = request.json()['href']

        with open(file_path, encoding='utf-8') as f:
            data = f.read()

        request_put = session.put(href, data=data.encode('utf-8'), headers=headers)
        #ну покрайней мере по моему токену я получил тестовый файл на яндекс.диске


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = 'uploads.txt'
    token = '' #запрещено передавать на гит
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)

