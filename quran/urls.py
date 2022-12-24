from django.contrib import admin
from django.urls import path, include
from quran.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('dashboard/', include('blog.urls')),
    path('about', about, name='about'),
    path('service', service, name='service'),
    path('contact', contact, name='contact'),
    path('blog', blog, name='blog'),
    path('login/', login, name='login'),
    path('logout/', logout_view, name='logout'),
]