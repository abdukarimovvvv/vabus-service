# VaBus Service

## Описание
Сервис для получения событий из шины данных VaBus, агрегации событий и отправки их в внешнее хранилище (PostgreSQL).

## Установка и Запуск

1. Клонируйте репозиторий:
    ```sh
    git clone https://github.com/yourusername/vabus-service.git
    cd vabus-service
    ```

2. Соберите Docker-образ:
    ```sh
    docker build -t vabus-service .
    ```

3. Запустите контейнер:
    ```sh
    docker run --env VABUS_URL=your_vabus_url --env POSTGRES_CONNECTION_STRING=your_postgres_connection_string --env AGGREGATION_TIME_WINDOW=60 vabus-service
    ```

## Конфигурация
Сервис настраивается с помощью переменных окружения:
- `VABUS_URL`: URL для подключения к шине данных VaBus.
- `POSTGRES_CONNECTION_STRING`: Строка подключения к базе данных PostgreSQL.
- `AGGREGATION_TIME_WINDOW`: Временное окно для агрегации событий (в секундах).

## Дополнительно
- Реализация агрегации событий и отправки данных в PostgreSQL приведена в виде сигнатур функций.
- Реальные реализации функций должны быть добавлены в соответствии с требованиями вашего проекта.
