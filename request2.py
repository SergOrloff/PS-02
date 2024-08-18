
# Задание 2: Параметры запроса

# Импортируем библиотеку requests для работы с HTTP-запросами
import requests

# Указываем URL для отправки GET-запроса
url = "https://jsonplaceholder.typicode.com/posts"

# Указываем параметры запроса, в данном случае userId равен 1
params = {
    'userId': 1
}

# Указываем параметры другого запроса, в этом случае userId равен 5
params1 = {
    'userId': 5
}

# Отправляем GET-запросы с указанными параметрами
response = requests.get(url, params=params)
response1 = requests.get(url, params=params1)

# Распечатываем полученные записи в формате JSON
print("Полученные записи для userId=1:", response.json())
print("Полученные записи для userId=5:", response1.json())