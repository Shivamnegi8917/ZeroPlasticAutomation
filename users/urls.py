from django.urls import path

from .views import home_view, signup_view, dashboard_view, rewards_view,shop_details_view, sastakaam

app_name = "users"

urlpatterns = [
    path('', home_view, name='home'),
    path('signup/', signup_view, name='sign-up'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('rewards/', rewards_view, name='rewards'),
    path('shopdetails/',shop_details_view,name='shopdetails'),
    path('showresult/', sastakaam, name='script processing' )
]
