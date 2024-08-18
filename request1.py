# Задание 1: Получение данных

# Импортируем библиотеку requests для работы с HTTP-запросами
import requests

# Указываем URL для отправки GET-запроса
url = "https://api.github.com/search/repositories"

# Указываем параметры запроса для поиска репозиториев с кодом html
params = {
    'q': 'language:html'
}

# Отправляем GET-запрос к API GitHub
response = requests.get(url, params=params)

# Распечатываем статус-код ответа. Код 200 указывает на успешное выполнение запроса
print("Статус-код ответа:", response.status_code)

# Распечатываем содержимое ответа в формате JSON. Это поможет увидеть структуру данных,
# которые мы получили
print("Содержимое ответа:", response.json())