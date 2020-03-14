import hello.views
from core.views import sync, home, coronafeed, test
from django.urls import path, include
from django.contrib import admin

admin.autodiscover()

urlpatterns = [
    path("", home, name="core_home"),
    path("test/", test, name="core_test"),
    path("api/coronafeed", coronafeed, name="corona-feed"),
    path("sync/", sync, name="core_sync"),
    path("admin/", admin.site.urls),

]