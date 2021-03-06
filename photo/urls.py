from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from photo import views

urlpatterns = [
    url(r"^location/(\w+)",views.location, name = "locations"),
    url(r'^locate',views.locate,name='location'),
    url(r'^$',views.index,name='landing'),
    url(r'^$',views.index,name='index'),
    url(r'^search/', views.search_results, name='search_results')

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)