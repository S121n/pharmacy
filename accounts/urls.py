from django.urls import path
from .views import signup , log_in , sign_out

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/',log_in, name='login'),
    path('logout/',sign_out,name='sign_out'),
]
