# Miel

Бекенд часть проекта для риелторской сети [Miel](https://miel.ru/)


## Установка и настройка

### 1. Клонирование репозитория

```bash
git clone https://github.com/AliakseiYafremau/Miel
cd Miel/backend
```

### 2. Установка зависимостей

```bash
python -m venv venv
source venv/bin/activate # Для Linux/MacOS
venv\Scripts\activate    # Для Windows
pip install -r requirements.txt
```

### 3. Настройка переменных окружения
Создайте файл `.env` в корневой директории проекта и заполните его переменными окружения согласно `example.env`

### 4. Создание базы данных
Создайте таблицы в базе данных с помощью `alembic`
```bash
alembic upgrade head
```

### 5. Заполение базы данных тестовыми полями
```bash
python -m app.utils.database.test_data
```

### 6. Запуск сервера

```bash
python -m app.main
```

Сервер доступен по адресу http://127.0.0.1:8000

### 7. Документация

- [Swagger UI](http://127.0.0.1:8000/docs)

- [Redoc](http://127.0.0.1:8000/redoc)

- [OpenAPI](http://127.0.0.1:8000/openapi.json)

### 8. Запуск тестов

```bash
pytest
```