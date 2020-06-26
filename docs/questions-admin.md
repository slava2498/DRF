Опросы
===
Во всех запросах - Headers Authorization Token ac223e430cba8ea551f17833c9806c90b09b5694

GET-запрос, http://127.0.0.1:8000/questions/
Возвращает список вопросов

POST-запрос, http://127.0.0.1:8000/questions/
Допустимые значения type_qustion - 'few', 'one', 'text'
Возвращает созданный объект

Тип ответа - несколько вариантов
```json
{
    "text": "как ты",
    "type_qustion": "few"',
    "options_id": "1,2,3"
}
```
Тип ответа - один вариант вариантов
```json
{
    "text": "как ты",
    "type_qustion": "one",
    "options_id": "1"
}
```
Тип ответа - текст
```json
{
    "text": "как ты",
    "type_qustion": "text"
}
```

PUT/PATCH-запрос, http://127.0.0.1:8000/questions/1
Возвращает обновлённый объект

Тип ответа - несколько вариантов
```json
{
    "text": "как ты1",
    "type_qustion": "few"',
    "options_id": "1,2"
}
```
Тип ответа - один вариант вариантов
```json
{
    "text": "как ты2",
    "type_qustion": "one",
    "options_id": "2"
}
```
Тип ответа - текст
```json
{
    "text": "как ты3",
    "type_qustion": "text"
}

DELETE-запрос, http://127.0.0.1:8000/questions/1
Удаляет объект

