"""t URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.template.backends import django
from django.urls import path, include

from j import views

urlpatterns = [
  url(r'^admin/', admin.site.urls),
  url(r'^$', views.base_view),
  url(r'^home', views.home_view,name='home'),
  url(r'^index', views.show_view),
  url(r'^activity', views.activity_view),
  url(r'^insert/', views.insert_view),
  url(r'^delete/(?P<id>\d+)/$', views.delete_view),
  url(r'^update/(?P<id>\d+)/$', views.update_view),
  url(r'^addactivity/', views.activityinsert_view),
  url(r'^deactivity/(?P<id>\d+)/$', views.activitydelete_view),
  url(r'^upactivity/(?P<id>\d+)/$', views.activityupdate_view),
  path('accounts/',include('django.contrib.auth.urls' )),
  url(r'^login/', views.login_view),
  url(r'^logout/', views.logout_view),  

  ]
if settings.DEBUG:
 urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
