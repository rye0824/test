from django.contrib import admin
from django.urls import path
import appname.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', appname.views.home, name='home'),
]
