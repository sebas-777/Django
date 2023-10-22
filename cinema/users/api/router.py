from django.urls import path
from users.api.views import ResgisterView

urlpatterns = [
    path('auth/register', ResgisterView.as_view())
]