module 1:

Для запуска сервера:
1) Установить Python
2) Установка зависимостей
	a) С .venv
		1) Открыть консоль в корневой папке и ввести команды по очереди:
		python -m venv .venv
		.\.venv\Scripts\activate.bat
		pip install -r requirements.txt
	б) Без .venv 
		1) Открыть консоль в корневой папке и ввести команду:
		pip install -r requirements.txt
3) Запуск сервера
	а) Автоматический
		1) Запустить runServer.bat
	б) Ручной
		a) С .venv
			1) Открыть консоль в корневой папке и ввести команды по очереди:
			.\.venv\Scripts\activate.bat
			cd .\trains\
			python manage.py runserver
		b) Без .venv
			1) Открыть консоль в корневой папке и ввести команды по очереди:
			cd .\trains\
			python manage.py runserver

Для запуска Swagger:
1) Установить Node.js
2) Запуск Swagger
	а) Автоматический
		1) Запустить runSwagger.bat
	б) Ручной
		1) Открыть консоль в корневой папке и ввести команды по очереди:
		cd .\trains\swagger\
		npm start

module 2:

(Считаю что далее не нужно указывать вариант с .venv при использовании Python)
1) Обновить зависимости
	a) Прописать в корневой папке:
	pip install -r requirements.txt
2) Создать свою бд (CREATE DATABASE name в SQL SHELL)
3) В .\trains\trains\settings.py в 81:90 (параметр DATABASES) строчках необходимо заполнить данные о своей бд.
4) Очистить папку .\trains\api\migrations\ оставив там только __init__.py
5) Из корневой папки переходим в .\trains\ и вводим последовательно команды:
python .\manage.py makemigrations
python .\manage.py migrate
python .\manage.py loaddata .\fixtures\data.json


module 3:

Созданы 2 аккаунта log: admin, pas: admin и log: RouteMod, pas: TestAdmin
1) Очистить бд и загрузить фикстуры 
python .\manage.py loaddata .\fixtures\data.json
2) Запустить сервер
python manage.py runserver
3) Перейти по ссылке:
http://127.0.0.1:8000/admin/
4) Ввести данные аккаунта или супер админа или администратор расписания

module 4:

1) Ввести стандартные команды для обновления:
pip install -r requirements.txt
python .\manage.py makemigrations
python .\manage.py migrate
python .\manage.py loaddata .\fixtures\data.json
2) Запустить сервер
3) Регистрация нового пользователя
Отправляем пост запрос с данными аккаунта по пути:
http://127.0.0.1:8000/security/registration/
Например:
{
    "username": "TestUser2",
    "password1": "TestAdmin",
    "password2": "TestAdmin"
}
4) Скопировать access токен и теперь можно "купить" билет, для этого сделать пост запрос по пути:
http://127.0.0.1:8000/api/tickets
Например:
{
    "train_route": 2,
    "user": 3
}


