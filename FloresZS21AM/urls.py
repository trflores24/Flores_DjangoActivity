from django.contrib import admin
from django.urls import path
from members.views import members

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', members),
]