from django.contrib import admin
from django.urls import path, include
import Preoperacional_app
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Preoperacional_app.urls'))
]

if settings.DEBUG == True:
    urlpatterns == static(settings.MEDIA_URL, document_url=settings.MEDIA_ROOT)