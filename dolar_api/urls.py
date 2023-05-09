from django.contrib import admin
from dolar.views import cotacao_dolar, cotacao_real
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cotacao-dolar/', cotacao_dolar, name='cotacao_dolar'),
    path('cotacao-real/', cotacao_real, name='cotacao_real'),
]
