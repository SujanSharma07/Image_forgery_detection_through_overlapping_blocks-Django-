from django.conf.urls import url
from . import views

app_name = 'detect'
urlpatterns=[
    url(r'^$', views.detect, name='detector'),
    url(r'predict', views.detect, name='detector'),

    # url(r'^logout/$',views.user_logout,name='logout'),
   # url(r'^profile/(?P<pk>\d+)/$', views.ProfileDetailView.as_view(), name='profile'),

]
