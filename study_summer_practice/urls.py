from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from cms.views import start_page, about_page, team_page, projects_page, contact_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', start_page, name='index'),
    path('about/', about_page, name='about'),
    path('team/', team_page, name='team'),
    path('projects/', projects_page, name='projects'),
    path('contact/', contact_page, name='contact'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
