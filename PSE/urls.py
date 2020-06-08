from django.contrib import admin
from django.urls import path, include
from painel import urls as painel_urls
from login import urls as login_urls

urlpatterns = [
    path('', include(login_urls)),
    path('painel/', include(painel_urls)),
    path('admin/', admin.site.urls),
    path('django_plotly_dash/', include('django_plotly_dash.urls')),
]
