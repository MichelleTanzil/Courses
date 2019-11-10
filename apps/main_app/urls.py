from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^add_course$', views.add_course),
    url(r'^courses/destroy/(?P<course_id>\d+)$', views.course_profile),
    url(r'^DNDestroy$', views.DNDestroy),
    url(r'^destroy_course/(?P<course_id>\d+)$', views.destroy_course),
]
