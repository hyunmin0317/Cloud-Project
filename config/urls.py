from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include

import hip.views
from config import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', hip.views.home, name='home'),
    path('hip/', include('hip.urls')),
    path('place/', include('place.urls')),
    path('accounts/', include('allauth.urls')),
    path('logout/', auth_views.LogoutView.as_view(), name='logout')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)