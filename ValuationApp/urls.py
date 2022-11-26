from django.urls import path

from ValuationApp import views

urlpatterns = [
                  path('ValuationApi/<str:symb>', views.valuation_detail, name='main'),
              ]