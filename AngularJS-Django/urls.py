from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.decorators.csrf import csrf_exempt
from rest_framework import routers
from  accounts.RestViews import UserView
import accounts


#router = routers.DefaultRouter()
#router.register(r'users', )


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/',include('rest_framework.urls', namespace='rest_framework')),
    url(r'^users/', csrf_exempt(accounts.RestViews.UserView.as_view({
        'get': 'list',
        'post': 'create'
    })), name='user'),
    url(r'^token', 'accounts.views.token', name='token'),
    #url(r'^users/', 'accounts.views.users',name='users'),
    url(r'^login/', 'accounts.views.perform_login', name='login'), #why isn't this just /logout/?
    url(r'^login2/', 'accounts.RestViews.make_login', name='login2'),
    url(r'^check/login/', 'accounts.RestViews.current_login', name='check'),
    url(r'^register/', 'accounts.views.register', name='register'), #lets think about using premade django-registration here
    url(r'^logout/', 'accounts.views.perform_logout', name='logout'),
    url(r'social/', include('social.apps.django_app.urls', namespace='social')), # cool

)
