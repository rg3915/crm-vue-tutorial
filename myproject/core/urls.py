from django.urls import path
from myproject.core import views as v


app_name = 'core'


urlpatterns = [
    path('', v.customers, name='customers'),
    path('add/', v.customer_create, name='customer_create'),
]
