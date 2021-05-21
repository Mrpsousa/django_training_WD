from django.urls import path

from project.subscriptions.views import new, detail

app_name = 'subscriptions'
urlpatterns = [
    path('', new, name='new'),
    path('<int:pk>/', detail, name='detail'),
]
