@echo off
echo --- GLOBAL SETUP STARTED ---

:: Проверяем, есть ли папка backend
if exist "backend" (
    cd backend
    echo Found backend folder.
) else (
    echo Backend folder NOT found! Check your paths.
    pause
    exit
)

:: Создаем venv если нет
if not exist "venv" (
    echo Creating virtual environment...
    python -m venv venv
)

:: Ставим библиотеки
echo Installing requirements...
call venv\Scripts\activate && pip install -r requirements.txt

echo --- SETUP FINISHED! ---
pause