from django.contrib import admin
from django.urls import path, include
from challenges.views import index


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home-mypage'),
    path('challenges/', include('challenges.urls'))
]
