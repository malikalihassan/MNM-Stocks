
from django.urls import path

from StocksData import views

urlpatterns = [
                  path('MainApi/<str:symb>', views.stocks_detail, name='main'),
                  path('MainApi/', views.stocks_detail, name='main'),
                 path('PostApi/', views.post_data, name='post'),
              ]