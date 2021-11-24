from django.shortcuts import render, redirect
from .models import Gif, Category
# Create your views here.

def homepage(request):
    return render(request, 'homepage.html', {'gifs':Gif.objects.all()})


def category_view(request, category_id):
    cat = Category.objects.get(id=category_id)
    return render(request, 'category.html', {'category': cat})

def gif_view(request, gif_id):
    gif = Gif.objects.get(id=gif_id)
    return render(request, 'gif.html', {'gif': gif})

def categories_view(request):
    return render(request, 'categories.html', {'categories': Category.objects.all()})

def gif_like_action(request, gif_id, liked):
    gif = Gif.objects.get(id=gif_id)
    if liked:
        gif.likes += 1
    else:
        gif.likes -= 1
    gif.save()
    return redirect('single_gif', gif.id)
