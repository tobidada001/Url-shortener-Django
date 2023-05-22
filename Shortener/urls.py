from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name = 'index'),
    path('<str:part>', views.redirect_to_link, name = 'redirect_link')
]
