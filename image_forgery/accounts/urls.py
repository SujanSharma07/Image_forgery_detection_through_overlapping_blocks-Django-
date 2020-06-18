from django.conf.urls import url
from . import views
app_name = 'accounts'
urlpatterns=[
    url(r'^$', views.user_login, name='login'),
    #url(r'^signup$', views.signup, name='register'),
    url(r'register', views.register, name='register'),
    url(r'^logout/$',views.user_logout,name='logout'),
   # url(r'^profile/(?P<pk>\d+)/$', views.ProfileDetailView.as_view(), name='profile'),

]