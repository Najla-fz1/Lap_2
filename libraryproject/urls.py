from django.contrib import admin
import apps.bookmodule.views
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', include("apps.bookmodule.urls")), #include urls.py of bookmodule app
    path('users/', include("apps.usermodule.urls")) , #include urls.py of usermodule app
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


