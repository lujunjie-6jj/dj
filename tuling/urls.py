from django.conf.urls import include, url
from django.contrib import admin
from teacher import views as tn
from teacher import teacher_url
urlpatterns = [
    # Examples:
    # url(r'^$', 'tuling.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/',include(admin.site.urls)),
    url(r'^normalamb/', tn.normalamb),
    url(r'^teacher/',include(teacher_url)),

    #
    url(r'^date/(?P<year>[0-9]{4})/(?P<month>[0,1][0-9])',tn.withparam),

    #页码         ?:表明忽略此参数
    url(r'^book/(?:page_(?P<pn>\d+)/)$',tn.param),
    url(r'^name',tn.name,{'name':"lujunjei"}),

    url(r'^yoururl',tn.wangshi,name="askname")



]
