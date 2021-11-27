from django.contrib import admin
from django.urls import path
from Blog.views import homepage, about, blog, maqola
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name='home'),
    path('about/', about, name='about'),
    path('blog/', blog, name='blog'),
    path('blog/maqola/<int:son>', maqola, name='maqola'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
