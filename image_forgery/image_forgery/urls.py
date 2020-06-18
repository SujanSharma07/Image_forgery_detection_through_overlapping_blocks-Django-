from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from accounts import views
from accounts.views import Aboutpageview,Contactpageview
from image_forgery import settings

from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$',views.user_login,name='user_login'),
    url(r'register', views.register, name='register'),
    #class base page view is done using as_view()
    url(r'^about/',Aboutpageview.as_view(),name='about'),
    url(r'^contact/',Contactpageview.as_view(),name='contact'),


    url(r'^accounts/',include('accounts.urls')),
    url(r'^detector/',include('detect.urls')),
]


urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

