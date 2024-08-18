# Задание 3: Отправка данных

# Импортируем библиотеку requests для работы с HTTP-запросами
import requests
# Импортируем модуль pprint, которая нужна для более удобного чтения словарей при их выводе
import pprint

# Указываем URL для отправки POST-запроса
url = "https://jsonplaceholder.typicode.com/posts"

# Создаем словарь с данными, которые будем отправлять
data = {
    'title': 'foo',
    'body': 'bar',
    'userId': 1
}

# Отправляем POST-запрос с созданными данными
response = requests.post(url, json=data)

# Распечатываем статус-код ответа. Код 201 указывает на успешное создание ресурса
print("Статус-код ответа:")
pprint.pprint(response.status_code)

# Распечатываем содержимое ответа в формате JSON.
# Это поможет увидеть, как сервер обработал наши данные
print("Содержимое ответа:")
pprint.pprint(response.json())