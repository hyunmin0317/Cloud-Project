from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

import hip.views
from config import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', hip.views.home, name='home'),
    path('hip/', include('hip.urls')),
    path('place/', include('place.urls')),
    path('common/', include('common.urls')),
    path('accounts/', include('allauth.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)