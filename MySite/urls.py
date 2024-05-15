from django.contrib import admin
from django.urls import path, include
import Preoperacional_app
from django.conf import settings
from django.conf.urls.static import static


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
        path('admin/', admin.site.urls),
        path('', include('Preoperacional_app.urls')),
        path('SPV/', include('SPV_app.urls')),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
else:
    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('Preoperacional_app.urls')),
        path('SPV/', include('SPV_app.urls')),
    ]

if settings.DEBUG == True:
    urlpatterns == static(settings.MEDIA_URL, document_url=settings.MEDIA_ROOT)