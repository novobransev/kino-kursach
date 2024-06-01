import requests
import json

# Создаем пустой список для хранения данных
data = []

for i in range(301, 410):
    url = f'https://api.kinopoisk.dev/v1.4/movie/{i}'
    headers = {
        'X-API-KEY': 'AC8BFMV-RPV4M74-GEEPPBF-CYTJXA2',
        'Content-Type': 'application/json',
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        film_data = response.json()

        data.append(film_data)
        print(f'Данные для фильма {i} успешно добавлены.')
    except requests.exceptions.RequestException as e:
        print(f'Ошибка при получении данных для фильма {i}: {e}')

# Записываем данные в файл
with open('kinopoisk.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print('Все данные успешно записаны в файл kinopoisk.json.')

