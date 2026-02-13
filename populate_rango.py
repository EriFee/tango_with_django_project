import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')

import django
django.setup()

from rango.models import Category, Page


def add_page(cat, title, url, views=0):
    p, created = Page.objects.get_or_create(category=cat, title=title)
    p.url = url
    p.views = views
    p.save()
    return p


def add_cat(name, views=0, likes=0):
    c, created = Category.objects.get_or_create(name=name)
    c.views = views
    c.likes = likes
    c.save()
    return c


def populate():

    python_pages = [
        {'title': 'Official Python Tutorial', 'url': 'https://docs.python.org/3/tutorial/'},
        {'title': 'Python Package Index', 'url': 'https://pypi.org/'},
        {'title': 'Learn Python', 'url': 'https://www.learnpython.org/'},
    ]

    web_pages = [
        {'title': 'MDN Web Docs', 'url': 'https://developer.mozilla.org/'},
        {'title': 'W3Schools', 'url': 'https://www.w3schools.com/'},
    ]

    cats = {
        'Python': {'pages': python_pages, 'views': 128, 'likes': 64},
        'Web Development': {'pages': web_pages, 'views': 64, 'likes': 32},
    }

    for cat_name, cat_data in cats.items():
        c = add_cat(cat_name, views=cat_data['views'], likes=cat_data['likes'])
        for p in cat_data['pages']:
            add_page(c, p['title'], p['url'])

    for c in Category.objects.all():
        print(f"{c} - {c.slug}")
        for p in Page.objects.filter(category=c):
            print(f"  - {p.title}")


if __name__ == '__main__':
    print("Starting Rango population script...")
    populate()
