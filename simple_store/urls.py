from django.conf.urls import include, url
from store import urls as appurls
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', 'simple_store.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include(appurls)),
    url(r'^admin/', admin.site.urls),
]
