from django.conf.urls import url
from registration import views

urlpatterns = [
    url(r'^signup$', views.signup, name='registration_signup'),
    url(r'^signup_tags/(\w+)/(\d+)', views.select_initial_tags, name='registration_select_initial_tags')
]
