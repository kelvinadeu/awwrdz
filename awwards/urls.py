from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url,include
from django.conf.urls import url

from . import views

urlpatterns = [
    url('',views.signup, name='signup'),
    url('login',views.login, name='login'),
    url('^$',views.home,name = 'home'),
    # url(r'accounts/', include('django.registration.auth.urls'))

    # url('admin/',admin.site.urls)
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
