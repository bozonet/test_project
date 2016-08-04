# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from bildirge.views import register_view , home, login_view,logout_view,file_view, upload_file
from django.conf.urls import patterns, url
import bildirge.views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^home/', bildirge.views.home, name = 'home'),
    url(r'^register/', bildirge.views.register_view, name ='register' ),
    url(r'^kaydol/', bildirge.views.contact, name = 'kaydol'),
    #url(r'^kayit/', bildirge.views.total_register, name ='kayit' ),
    url(r'^home/', bildirge.views.home, name ='home' ),

    url(r'^login/', bildirge.views.login_view, name = 'login'),
    url(r'^upload/', login_required(bildirge.views.file_view), name = 'upload'),
    url(r'^uploadnew/', login_required(bildirge.views.upload_file), name = 'upload_file'),
	url(r'^logout/', logout_view, name='logout'),   

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT )