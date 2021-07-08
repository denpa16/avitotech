# Тестовое задание для стажера в юнит Market Intelligence

## Возможности JSON API сервиса
- Создать новое голосование с разными вариантами ответов 
- Отдать свой голос за какой-либо вариант (можно отвечать на несколько ответов сразу, если голосование с множественным выбором)
- Получить текущий результат голосования

## Методы взаимодействия с сервисом
- POST /api/createPoll/ создать голосование c вариантами ответов
- POST /api/poll/ проголосовать за конкретный вариант: <poll_id, choice_id>
- POST /api/getResult/ получить результат по конкретному голосованию: <poll_id>

### Формат данных

Для метода
«`POST /api/createPoll/ »
