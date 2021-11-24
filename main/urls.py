from django.urls import path
from . import views
urlpatterns = [
    path('', views.homepage, name='home'),
    path('categories/<int:category_id>/', views.category_view, name='single_cat'),
    path('gif/<int:gif_id>/', views.gif_view, name='single_gif'),
    path('gif/<int:gif_id>/<int:liked>', views.gif_like_action, name='like_link'),
    path('categories/', views.categories_view, name='categories')
]
