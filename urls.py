from django.urls import path

from .views import home_view

urlpatterns = [
    # path('members/', views.members, name='members'),
    path('home_view/',home_view,name='home_view'),
]