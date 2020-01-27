from django.urls import path

from .views import home_view, signup_view, dashboard_view, rewards_view

app_name = "users"

urlpatterns = [
    path('', home_view, name='home'),
    path('signup/', signup_view, name='sign-up'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('rewards/', rewards_view, name='rewards')
]
