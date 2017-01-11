# from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from mycaps.views import package_add

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', package_add, name='package'),
]
