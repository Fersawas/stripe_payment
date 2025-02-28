# STRIPE_PAYMENT
## Описание проекта
Проект stripe_payment позволяет оплачивать товары, создавать заказы и вносить оплату частично или полностью.
### Содержанеие

- [Технологии](#tech)
- [Начало работы](#begining)
- [Запуск через docker](#docker)
- [Основные эндпоинты и возможности](#endpoints)

## <a name="tech">Технологии</a>

- [Django](https://www.djangoproject.com/)
- [Docker](https://www.docker.com/)
- [Stripe](https://docs.stripe.com/api)

## <a name="begining">Начало работы</a>

### Начало работы

Активируйте вирутальное окржуние:

```
python -m venv venv
```

### Установка зависимостей
Активируйте виртуальное окружение

```
source venv/Scripts/activate
```

Установите зависимости из файла *requirements.txt*:

```
pip install -r requirements.txt
```
Настройте конфигурацию файла .env

### Запуск сервера
Примените миграции:

```
python manage.py makemigration
python manage.py migrate
```
Заполните проект тестовыми данными
```
python manage.py fill_db
```

Запустите проект:

```
python manage.py runserver
```
## <a name="docker">Запуск через docker</a>
Зайдите в корневую директорию
Запустите dockerfile:

```
docker compose -f docker-compose.yaml up -d
```

При этом запустятся миграции и заполнится бд


Создайте суперпользователя
```
make superuser
```

## <a name="endpoints">Основные эндпоинты и возможности</a>
Для просмотра товаров 
    http://localhost:8000/payment/items/

Для просмотра оплаты товара, перейдите на страницу конкретного товара 
    http://localhost:8000/payment/items/pk

Для оплаты заказа
    http://localhost:8000/payment/order/
