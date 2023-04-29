'''DRF'''
# API (Application programming interface)
# место соприкосновения клиента и сервера, предназначено для взаимодействия между программами

'''REST (representational state transfer)- стиль API, стандарт , которому следует API'''

# принципы REST
# 1. разграничивание клиента и сервера
# 2. отсутствие состояния (нет сохранения состояния)- сервер не должен хранить какую-либо информацию о клиенте
# 3. кеширование
# 4. многоуровневая система
# 5. единый интерфейс
# 6. код предоставляется по запросу

# RESTfull API - API которое соответствует принципам REST


# 1. Создаем виртуальное  окружение 
# python3 -m venv venv

# 2. Активируем виртуальное окружение 
#  . venv/bin activate

# 3. создаем файл req.txt
# записываем : Django, djangorestframework, psycopg2-binary

# 4. устанавливаем: pip3 install -r req.txt

# 5. django-admin startproject <название> . -> создание проекта, если не поставим точку, будет вложенность директорий

# 6. python3 manage.py startapp <app_name> - создание приложения

# 7. открываем файл settings.py в INSTALED_APPS -> регистрируем rest_framework, <app_name>

# 8. в файле settings.py настраиваем базу данных
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql', 'NAME': 'test', 'USER': 'hello', 'PASSWORD':1, 'HOST': 'localhost', 'PORT': 5432
#     }
# }

# 8. python3 manage.py makemigrations -> создает файл миграций
# 9. python3 manage.py migrate

# 10. python manage.py createsuperuser - создание суперпользователя (админ)
# 11. python3 mangage.py runserver -> запуск проекта
# 12. python3 mangage.py runserver 8001

'''Model'''

# как проходит запрос
# 1. asgi/wsgi -> (те которые принимают запрос и возвращают ответ)

# 2. settings -> middlewares
# 3. urls -> маршрутизаторы
# 4. views -> пердставление ( функции, которые возвращают данные в нужном формате)
# 5. serializers ( классы, которые переводят данные из json в python и наоборот )
# 6. models ( классы, которые обозначают как будет выглядеть наша таблица в БД)
# 7. managers (objects) -> классы, которые работают с ORM
# 8. db -> база данных

#========== Поля =========
#  'CharField' -> для строкового значения(обьязательно нужно указывать max_length)
#  'SlugField' -> для хранения  slug ( обычно используется в url) содержит только буквы, числа, -, _
#  'TextField' -> для хранения текста
#  'DecimalField' -> для дробных чисел (max_digit: кол-во цифр целой части)
#  decimal_places (кол-во цифр после запятой))
#  'IntegerField' -> для чисел
#  'BooleanField'  -> для bool значений
#  'DataField'  -> для дат (datetime.date) можно передать аргументы: auto_now -> обновляется при изменнении записи
# auto_now_add  -> задается только при создании
#  'TimeField' -> для времени (auto_now, auto_now_add)
#  'DateTimeField' -> для даты и времени
#  'EmailField' -> для email
#  'FileField' -> для файлов (upload_to -> указание директории, где будет хранится файл)
#  'ImageField' -> для картинок
#  'JSONField'  -> для строк в формате json

'''Ключевые  параметры для полей (опции)'''
#  null -> если  True, будет в бд записывать null, если данные переданы
#  blank ->  если True, будет ставить пустую строку (не обязательно для заполнения)
#  default -> значение по умолчанию
#  unique -> если True, в колонке могут хранится только уникальные значения
#  primary_key -> если True, первичный ключ - идентификатор
#  choices -> список с  tuple (ограничывам возможные варианты для заполнения)



'''======Связи======='''
# ForeignKey ->  связь один ко многим (обьязательно указать модель на которую мы будем ссылаться, on_delet, related_name - для обратной связи)

# ManyToManyField ->  многи ко многим (все то же самое, что и ForeignKey)

'''========= on_delete ========='''
# models.CASCADE -> каскадное удаление ( если уудаляется главный обьект, то удаляется и зависящие от него)
# model.PROTECT -> вызывает ошибку при попытке удалить главный обьект
# model.SET_NULL -> не удаляет зависящие обьекты, а ставит null (null=True)
#  models.SET_DEFAULT -> если определен default, то ставит его
#  models.DO_NOTHING -> ничего неделает, вызывается ошибка

''''==================='''
# Product.objects.all()
# # SELECT * FROM products;
#
# Product.objects.get(id=1)
# SELECT * FROM products WHERE id = 1;

# Product.objects.filter(условие1, условие2)
# SELECT * FROM products WHERE условие AND условие2;

# Product.objects.filter(Q(условие)|Q(условие2))
# SELECT * FROM products WHERE условие1 OR условие2;

# Product.objects.filter(~Q(условие))
# Product.objects.exclude(условие)
# SELECT * FROM products WHERE NOT условие;

# Product.objects.filter(price__gt=50000) #больше
# SELECT * FROM products WHERE price > 50000;

# Product.objects.filter(price__lt=50000) #меньше
# SELECT * FROM products WHERE price < 50000;

# Product.objects.filter(price=50000) #равно
# SELECT * FROM products WHERE price = 50000;

# Product.objects.filter(~Q(price=50000))
# SELECT * FROM products WHERE NOT price = 50000;

# Product.objects.filter(price__gte=50000)
# SELECT * FROM products WHERE price >= 50000;

# Product.objects.filter(price__lte=50000)
# SELECT * FROM products WHERE price <= 50000;

# Product.objects.filter(category_id__in=['phones', 'notebooks'])
# SELECT * FROM product WHERE category_id IN ('phones', 'notebooks');

# Product.objects.filter(price__range=[20000, 50000])
# SELECT * FROM products WHERE price BETWEEN 20000 AND 50000;

# Product.objects.filter(name__exact='Iphone')
# SELECT * FROM products WHERE name LIKE 'Iphone';
# Product.objects.filter(name__iexact='Iphone')
# SELECT * FROM products WHERE name ILIKE 'Iphone';

# Product.objects.filter(name__startswith='Iphone')
# SELECT * FROM products WHERE name LIKE 'Iphone%';
# Product.objects.filter(name__istartswith='Iphone')
# SELECT * FROM products WHERE name ILIKE 'Iphone%';

# Product.objects.filter(name__contains='Iphone')
# SELECT * FROM products WHERE name LIKE '%Iphone%';
# Product.objects.filter(name__icontains='Iphone')
# SELECT * FROM products WHERE name ILIKE '%Iphone%';

# Product.objects.filter(name__endswith='Iphone')
# SELECT * FROM products WHERE name LIKE '%Iphone';
# Product.objects.filter(name__iendswith='Iphone')
# SELECT * FROM products WHERE name ILIKE '%Iphone';

# Product.objects.order_by('price')
# SELECT * FROM products ORDER BY price ASC;

# Product.objects.order_by('-price')
# SELECT * FROM products ORDER BY price DESC;

# Product.objects.only('name')
# SELECT name FROM products;

# Product.objects.only('name', 'price') #запрашивает указанные поля
# SELECT name, price FROM products;

# Product.objects.defer('name', 'price') #исключает указанные поля
# SELECT id, description, category_id FROM products;

# Product.objects.count()
# SELECT COUNT(*) FROM products;

# Product.objects.filter(...).count()
# SELECT COUNT(*) FROM products WHERE ...;

# Product.objects.create(name='Apple Iphone 12',
                    #    description='awddwdawd',
                    #    price=78000,
                    #    category_id='phones')
# INSERT INTO products (name, description, price, category_id) VALUES \
    # ('Apple Iphone 12', 'dwadaafafaw', 78000, 'phones');

# Product.objects.bulk_create([
    # Product(...),
    # Product(...)
# ]) #множественное создание

# Product.objects.update(price=50000)
# UPDATE products SET price=50000;

# Product.objects.filter(...).update(price=50000)
#UPDATE products SET price=50000 WHERE ...;

# Product.objects.filter(id=1).update(price=50000)
#UPDATE products SET price=50000 WHERE id=1;

# product = Product.objects.get(id=1)
# product.price = 50000
# product.save()

# Product.objects.delete()
# DELETE FROM products;

# Product.objects.filter(category_id='phones').delete()
# DELETE FROM products WHERE category_id = 'phones';

# Product.objects.filter(id=1).delete()
# DELETE FROM products WHERE id=1;

# product = Product.objects.get(id=1)
# product.delete()

'''===================='''

'''related_name'''
# позволяет обращаться из связанных обьектов к тем, от которых эта связь создана (для обратного поиска)
# realted_name -> создает свзь с обратной стороны

# cat = Category.objects.get(id=1)
# cat.posts.all() -> получение всех постов, относящихся к данной категории.


'''related_query_name = post'''
# создает именнованый атрибут, который позволяет делать запросы с использованием метода perfetch_related -> загружает связанные обьекты (оптимизирует запросы в бд)
# cat.post.all()

# QuerySet -> обьекты полученные из базы данных, благодаря manager'y

# Manager -> класс, предоставляет методы для доступа к ORM Django(отправляет запрос в бд)
# default = objects
# (обновляем , получаем, удаляем, фильтруем, данные из таблиц)
# >>> p = Post.objects.get(id=1)
# >>> p.tags.add(t)
# >>> p2 = Post.objects.get(id=3)
# >>> p2.tags.add(t)



# python3 manage.py shell

# sudo lsof -t -i tcp:8000 | xargs kill -9