# Дипломный проект. Задание 2: Тестирование REST API

## Автотесты для UI сервиса Stellar Burgers

## Реализованные сценарии

### Общие моменты

* Необходимо использовать паттерн "Page Object"
* Протестировать функциональность в Google Chrome и Mozilla Firefox

### Восстановление пароля

- переход на страницу восстановления пароля по кнопке «Восстановить пароль»,
- ввод почты и клик по кнопке «Восстановить»,
- клик по кнопке показать/скрыть пароль делает поле активным --- подсвечивает его.

### Личный кабинет

- переход по клику на «Личный кабинет»,
- переход в раздел «История заказов»,
- выход из аккаунта.

### Проверка основного функционала

- переход по клику на «Конструктор»,
- переход по клику на «Лента заказов»,
- если кликнуть на ингредиент, появится всплывающее окно с деталями,
- всплывающее окно закрывается кликом по крестику,
- при добавлении ингредиента в заказ, увеличивается счётчик данного ингредиента
- авторизованный пользователь может оформить заказ.

### Раздел «Лента заказов»

- если кликнуть на заказ, откроется всплывающее окно с деталями,
- заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»,
- при создании нового заказа счётчик **Выполнено за всё время** увеличивается,
- при создании нового заказа счётчик **Выполнено за сегодня** увеличивается,
- после оформления заказа его номер появляется в разделе **В работе.**



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
