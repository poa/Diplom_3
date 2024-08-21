# Дипломный проект. Задание 2: Тестирование REST API

## Автотесты для UI сервиса Stellar Burgers

## Реализованные сценарии


## Структура проекта

- `page` - модули c моделями страниц
- `tests` - пакет, содержащий тесты, разделённые по классам. 

## Запуск автотестов

Установка зависимостей

```shell
pip install -r requirements.txt
```

Запуск тестов с подробным выводом в консоль

```shell
pytest -v
```

Запуск тестов с формированием отчёта allure

```shell
pytest -v --alluredir=allure-results
```

Просмотра отчёта allure (allure предварительно должен быть [установлен](https://allurereport.org/docs/install/))

```shell
allure serve allure-results
```
