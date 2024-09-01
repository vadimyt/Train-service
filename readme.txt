Быстрый старт:
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
3) Установить настройки БД и почтового сервера в .\trains\trains\settings.py
4) Последовательно ввести команды, для миграции БД и загрузки фикстур:
python .\manage.py makemigrations
python .\manage.py migrate
python .\manage.py loaddata .\fixtures\data.json
5) Запуск сервера
	а) Автоматический
		1) Запустить runServer.bat
	б) Ручной
		1) Открыть консоль в корневой папке и ввести команды по очереди:
		cd .\trains\
		python manage.py runserver
6) Для входа в админ панель создан super admin:
username: admin
password: admin
И RouteMod:
username: RouteMod
password: TestAdmin
7) Для регистрации новых аккаунтов требуется подтверждение по почте, поле username для регистрации необязательно. Пример: пост запрос по пути http://127.0.0.1:8000/security/registration/
{
    "email": "example@example.ru",
    "password1": "TestAdmin",
    "password2": "TestAdmin"
}
Для входа в аккаунт запрос пост по пути http://127.0.0.1:8000/security/login/
{
    "email": "example@example.ru",
    "password": "TestAdmin"
}
8) По пути http://127.0.0.1:8000/swagger/ можно посмотреть документацию