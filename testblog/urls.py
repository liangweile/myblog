from testblog import views
from django.conf.urls import url


urlpatterns = [
    url(r'home$', views.home),
    url(r'category/(?P<category_name>\S+)', views.get_category ),
    url(r'post/(?P<post_name>\S+)', views.get_post_byname, name='post_url'),
    url(r'about$', views.about),
    url(r'post', views.get_post),
    url(r'signup', views.signup),
    url(r'signin', views.signin),
]