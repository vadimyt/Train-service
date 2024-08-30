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