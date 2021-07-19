from django.urls import path
from mainapp.views import mainTemplateView

app_name = 'mainapp'

urlpatterns = [
    path('', mainTemplateView.as_view(), name='home'),
]