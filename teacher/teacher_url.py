from django.conf.urls import include, url
from . import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'tuling.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'ljj/',views.ljj),



]