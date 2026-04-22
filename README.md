# Code Trainer Project - Backend (API)

Данный репозиторий содержит серверную часть платформы для решения задач по программированию. Проект выполнен в рамках учебного курса "Web Programming" (KBTU).

## Технологический стек
* **Python 3.12+**
* **Django 6.0** (Web Framework)
* **Django REST Framework** (API)
* **SQLite** (Database)

## Основные возможности (Features)
- **Authentication**: Система входа по токенам (Token Authentication).
- **Categories & Tasks**: Просмотр списка задач по категориям.
- **Submissions (Full CRUD)**: Студенты могут отправлять решения, просматривать свою историю, редактировать и удалять черновики.
- **Custom Logic**: Использование кастомных менеджеров моделей и валидаторов данных.

## Инструкция по запуску

1. **Создание виртуального окружения:**
   ```bash
   python -m venv venv
   .\venv\Scripts\activate

2. **Установка зависимостей:**
    ```bash
    pip install -r requirements.txt

3. **Применение миграций и запуск:**
    ```bash
    python manage.py migrate
    python manage.py runserver

## API Эндпоинты
- POST /api/login/ - Авторизация и получение токена.
- GET /api/categories/ - Список всех разделов задач.
- GET /api/categories/<id>/tasks/ - Список задач в конкретном разделе.
- GET/POST /api/submissions/ - Просмотр и создание решений (требуется Токен).
- GET/PUT/DELETE /api/submissions/<id>/ - Управление конкретным решением.