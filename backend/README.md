# Miel

Бекенд часть проекта для риелторской сети [Miel](https://miel.ru/)


## Установка и настройка

### 1. Клонирование репозитория

```bash
git clone https://github.com/MIEL-team-7/Backend
cd Backend
git switch dev
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


## Запуск с Docker-compose
Создайте файл `.env.docker` в корневой директории проекта и заполните его переменными окружения согласно `example.env`

### Запуск:
```bash
docker-compose up
```
### Остановка:
```bash
docker-compose stop
```

## Разработка

Разработка проходит в ветке `dev`
```bash
git switch dev # Для того, чтобы перейти в ветку dev
git branch --set-upstream-to origin/dev # Для того, чтобы указать ветку dev как ветку по умолчанию
git pull origin dev # Для того, чтобы обновить ветку dev
git push origin dev # Для того, чтобы отправить ветку dev
```

Работа с ветками
```bash
git branch <название_ветки> # Для того, чтобы создать ветку <название_ветки>
git switch <название_ветки> # Для того, чтобы перейти в ветку <название_ветки>
git push origin <название_ветки> # Для того, чтобы запушить ветку <название_ветки>
```

Работа с `ruff`
```bash
ruff check --fix # Запуск Ruff с автоматическим исправлением
ruff format      # Запуск Ruff для форматирования кода
```