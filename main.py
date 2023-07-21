
# Домашняя работа на 22.07.2023 (Результат при запуске)

'''
Задание 1. Создайте макроопределение для отображения списка пользователей в HTML-документе.
У вас есть список пользователей в переменной users, каждый пользователь представлен
в виде словаря с ключами name и email.
Используйте цикл for и условие if для отображения пользователей,
у которых почта кончается на gmail.com
'''

# Решение:

from jinja2 import Template

persons = [
    {'name': 'Георгий', 'email': 'Georg@gmail.com'},
    {'name': 'Виталий', 'email': 'Vital@mail.ru'},
    {'name': 'Алексей', 'email': 'Alex@yandex.ru'},
    {'name': 'Максим', 'email': 'Max@ya.ru'},
    {'name': 'Владимир', 'email': 'Vladim@mail.ru'},
    {'name': 'Александр', 'email': 'Sahs@gmail.com'}
]

html = """
{%- macro list_users(users) -%}
<ul>
    {% for u in users -%}
        {% if 'gmail.com' in u.email %}
            <li>{{ u.name }}</li>
        {% endif %}
    {%- endfor %}
</ul>
{% endmacro %}

{{ list_users(users) }}
"""

tm = Template(html)
msg = tm.render(users=persons)
print()
print('Решение задания 1:')
print()
print(msg)
print()



'''
Задание 2
Создайте макроопределение для отображения списка продуктов в HTML-документе.
У вас есть список продуктов в переменной products, каждый продукт представлен в виде словаря
с ключами name и price. Используйте цикл for и условие elif для отображения цены в зависимости от диапазона:
Если цена меньше 10, то пишем, что продукт доступный
Если цена меньше 20, то пишем, что продукт имеет среднюю цену
И если цена больше, то пишем, что продукт дорогой
'''

# Решение:

from jinja2 import Template

products = [
    {'name': 'Brad', 'price': 9},
    {'name': 'Sausage', 'price': 25},
    {'name': 'Milk', 'price': 15},
    {'name': 'Cucumber', 'price': 13},
    {'name': 'Tomato', 'price': 18},
    {'name': 'Potato', 'price': 7},
    {'name': 'Butter', 'price': 22},
    {'name': 'Salt', 'price': 5},
]

html = """
{% macro list_products(products) %}
<ul>
    {%- for p in products %}
        {%- if p.price < 10 %}
            <li>{{ p.name }} - продукт доступный</li>
        {%- elif p.price >= 10 and p.price < 20 %}
            <li>{{ p.name }} - продукт имеет среднюю цену</li>
        {%- else %}
            <li>{{ p.name }} - продукт дорогой</li>
        {%- endif -%}
    {% endfor %}
</ul>
{% endmacro %}

{{ list_products(products) }}
"""

tm = Template(html)
msg = tm.render(products=products)
print('-'*100)
print()
print('Решение задания 2:')
print()
print(msg)
print()

''' 
Задание 3. Потренероваться с выводом разметки:
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Домашнее задание</title>
</head>
<body>

<h1>Страница с домашним заданием</h1>
<p>Домашнее задание выполнено</p>

</body>
</html>
'''

# Решение:

from jinja2 import Environment, FileSystemLoader

file_loader = FileSystemLoader('templates')

env = Environment(loader=file_loader)

tm = env.get_template('final_page.html')

msg = tm.render(hometask='Домашнее задание', homework_page='Страница с домашним заданием',
                homework_completed='Домашнее задание выполнено!!!')
print('-'*100)
print()
print('Решение задания 3:')
print()
print(msg)
print()