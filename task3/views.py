from django.shortcuts import render


# Create your views here.
def platform_page(request):
    title = 'BookShop'
    name = 'Главная страница'
    context = {
        'title': title,
        'name': name,
    }
    return render(request, 'third_task/platform.html', context)


def books_page(request):
    title = 'Книги'
    name = 'Книги'
    text1 = 'Жюль Верн "Таинственный остров"'
    text2 = 'Г.Ф. Лавкрасфт "Хребты безумия"'
    text3 = 'Теодор Драйзер "Трилогия желаний"'
    context = {
        'title': title,
        'name': name,
        'text1': text1,
        'text2': text2,
        'text3': text3,
    }
    return render(request, 'third_task/books.html', context)


def cart_page(request):
    title = 'Корзина'
    name = 'Корзина'
    context = {
        'title': title,
        'name': name
    }
    return render(request, 'third_task/cart.html', context)
