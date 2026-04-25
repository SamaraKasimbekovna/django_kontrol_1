from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('myShop/', include('myShop.urls')),

    path('CineBoard/', include('CineBoard.urls')),
       
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)