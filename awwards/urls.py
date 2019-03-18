from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url,include
from . import views

urlpatterns = [
    url('',views.signup, name='signup'),
    url('login/',views.login, name='login'),
    # url(r'accounts/', include('django.registration.auth.urls'))

    # url('admin/',admin.site.urls)

]
