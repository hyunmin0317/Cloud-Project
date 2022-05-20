from django.contrib import admin
from django.urls import path, include

import hip.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', hip.views.home),
    path('hip/', include('hip.urls')),
    path('place/', include('place.urls')),
]
