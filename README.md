# Тестовый сервис на Flask


## Запуск

### С докером

```bash
cp example.env .env
docker compose up -d
```

### Без докера

- запустить postgress с помощью докера `docker compose up -d postgres`
- или другим способом, указав host, port, user и password в `.env` файле

```bash
cp example.env .env
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
python -m app.main
```

##### Миграции выполнятся автоматически
#### API будет доступен на порту 5000

---
# Документация API
Так же доступна [коллекция Postman](https://github.com/skrepkaq/Test-Flask-Task/blob/main/postman-collection.json) со всеми методами

## Формат ответа

### При успехе
```json
HTTP 200
{
    "cached": "Sat Mar 29 08:38:37 2025",  // если ответ был получен из кэша
    "result": ...
}
```
### При неудаче
```json
HTTP 400
{
    "error": "Сообщение об ошибке"
}
```

---

## Товары

### Получение списка всех товаров
**GET /api/products**

#### Описание:
Возвращает список всех товаров.

#### Пример запроса:
```http
GET /api/products
```

#### Пример ответа:
```json
{
    "result": [
        {
            "category": "Электроника",
            "id": 1,
            "name": "Смартфон"
        },
        ...
    ]
}
```

---

### Создание нового товара
**POST /api/products**

#### Описание:
Создаёт новый товар.

#### Параметры:
- `name` (string, required) - Название товара
- `category_id` (int, required) - ID категории

#### Пример запроса:
```http
POST /api/products?name=Проектор&category_id=1
```

#### Пример ответа:
```json
{
    "result": {
        "category": "Электроника",
        "id": 43,
        "name": "Проектор"
    }
}
```

---

### Обновление товара
**PUT /api/products/{product_id}**

#### Описание:
Обновляет данные существующего товара.

#### Параметры:
- `product_id` (int, required) - ID товара
- `name` (string, optional) - Новое название товара
- `category_id` (int, optional) - Новый ID категории

(необходимо указать как минимум один параметр из name, category_id)

#### Пример запроса:
```http
PUT /api/products/43?name=Сломанный проектор&category_id=5
```

#### Пример ответа:
```json
{
    "result": {
        "category": "Игрушки",
        "id": 43,
        "name": "Сломанный проектор"
    }
}
```

---

### Удаление товара
**DELETE /api/products/{product_id}**

#### Описание:
Удаляет товар по его ID.

#### Параметры:
- `product_id` (int, required) - ID товара

#### Пример запроса:
```http
DELETE /api/products/43
```

#### Пример ответа:
```json
{
    "result": "Товар успешно удалён"
}
```

---

## Аналитика

### Получение количества продаж за период
**GET /api/sales/total**

#### Описание:
Возвращает количество продаж за указанный период.

#### Параметры:
- `start_date` (string, required) - Дата начала периода (формат YYYY-MM-DD)
- `end_date` (string, required) - Дата окончания периода (формат YYYY-MM-DD)

#### Пример запроса:
```http
GET /api/sales/total?start_date=2025-01-01&end_date=2025-12-31
```

#### Пример ответа:
```json
{
    "result": 28307
}
```

---

### Получение самых продаваемых товаров за период
**GET /api/sales/top-products**

#### Описание:
Возвращает список самых продаваемых товаров за указанный период.

#### Параметры:
- `start_date` (string, required) - Дата начала периода (формат YYYY-MM-DD)
- `end_date` (string, required) - Дата окончания периода (формат YYYY-MM-DD)
- `limit` (int, required) - Количество возвращаемых товаров

#### Пример запроса:
```http
GET /api/sales/top-products?start_date=2025-01-01&end_date=2025-12-31&limit=10
```

#### Пример ответа:
```json
{
    "result": [
        {
            "count": 1179,
            "product": {
                "category": "Электроника",
                "id": 2,
                "name": "Ноутбук"
            }
        },
        ...
    ]
}
```
