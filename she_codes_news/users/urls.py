from django.urls import path
from .views import CreateAccountView
from .views import UserView

app_name = 'users'

urlpatterns = [
    path('create-account/', CreateAccountView.as_view(), name='createAccount'),
    path('<int:pk>/',UserView.as_view(),name='userProfile')
]