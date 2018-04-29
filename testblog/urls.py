from testblog import views
from django.conf.urls import url


urlpatterns = [
    url(r'home$', views.home),
    url(r'category/(?P<category_name>\S+)', views.get_category),
]