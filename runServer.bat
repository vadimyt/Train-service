@echo off
if exist .\.venv\Scripts\activate.bat call .\.venv\Scripts\activate.bat
cd .\trains\
python manage.py runserver
if  errorlevel 1 goto ERROR

:ERROR
echo Not all packages installed.
pause
