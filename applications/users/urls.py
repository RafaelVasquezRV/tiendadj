# django
from django.urls import path

# local
from . import views

app_name='users_app'

urlpatterns = [
    path(
        'login/', 
        views.LoginUserView.as_view(),
        name='login'
    ),
]