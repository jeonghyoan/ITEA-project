from django.urls import path

from accountapp.views import signup, login, logout

app_name = "accountapp"

urlpatterns = [
   path('signup/', signup, name='signup'),

   path('login/', login, name='login'),
   path('logout/', logout, name='logout'),
]