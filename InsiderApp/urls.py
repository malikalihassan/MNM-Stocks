from django.urls import path

from InsiderApp import views

urlpatterns = [
                  path('InsiderApi/<str:symb>/<int:costLimit>', views.insider_detail, name='insider_detail'),
              ]