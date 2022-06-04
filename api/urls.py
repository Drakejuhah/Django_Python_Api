from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from backend import views
from django.urls import path, include

urlpatterns = [

    path('admin/', admin.site.urls),
    path('products', views.all_products)

]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
