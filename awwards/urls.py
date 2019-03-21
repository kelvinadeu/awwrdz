from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url,include
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$',views.signup, name='signup'),
    url(r'login',views.login, name='login'),
    url(r'profile',views.profile, name='profile'),
    url(r'^search/', views.search_results, name='search_results'),
    url('',views.home,name = 'home'),
    url(r'^new_projects/$', views.new_projects, name='new_projects'),


    # url('admin/',admin.site.urls)
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
