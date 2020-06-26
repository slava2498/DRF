Опросы
===
GET-запрос, http://127.0.0.1:8000/polls/
Возвращает список опросов

POST-запрос, http://127.0.0.1:8000/polls/
Возвращает созданный объект
```json
{
    "name": "Опрос",
    "description": "опрос",
    "date_start": "2020-06-24",
    "date_end": "2020-06-25"
}
```
PUT/PATCH-запрос, http://127.0.0.1:8000/polls/1
Возвращает обновлённый объект
```json
{
    "name": "Опрос",
    "description": "опрос",
    "date_start": "2020-06-24",
    "date_end": "2020-06-25"
}
```

DELETE-запрос, http://127.0.0.1:8000/polls/1
Удаляет объект
