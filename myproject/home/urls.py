from django.urls import path
from . import views as v

urlpatterns = [
    path('', v.home, name='homepage'),
    path('about/', v.about, name='aboutpage'),
    path('viewdata/', v.viewdata, name='viewdata'),
    path('addhtmldata/', v.addhtmldata, name='addhtmldata'),
]