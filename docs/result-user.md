Опросы
===

GET-запрос, http://127.0.0.1:8000/result_polls/
Возвращает результаты
```json
{
    "user_id": "1",
    "poll_id": "1"'
}
```
Возвращает
```json
[
    {
        "question_text": "Кто ты",
        "text": "3,4"
    },
    {
        "question_text": "Как тебя звать",
        "text": "Заяц"
    },
    {
        "question_text": "Как дела",
        "text": "Восхитительно, Средне, "
    }
]
```

