Опросы
===
GET-запрос, http://127.0.0.1:8000/questions/
Возвращает список вопросов

POST-запрос, http://127.0.0.1:8000/questions/
Допустимые значения type_qustion - 'few', 'one', 'text'
Возвращает созданный объект

Тип ответа - несколько вариантов
```json
{
    "text": "как ты",
    "type_qustion": 'few',
    "options_id": "1,2,3"
}
```
Тип ответа - один вариант вариантов
```json
{
    "text": "как ты",
    "type_qustion": 'one',
    "options_id": "1"
}
```
Тип ответа - текст
```json
{
    "text": "как ты",
    "type_qustion": 'text'
}
```

PUT/PATCH-запрос, http://127.0.0.1:8000/questions/1
Возвращает обновлённый объект
```json
{
    "text": "как ты",
    "type_qustion": 'few',
    // "options_id": "1,2,3"
}
```

DELETE-запрос, http://127.0.0.1:8000/questions/1
Удаляет объект

