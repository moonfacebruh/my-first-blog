from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
]
#we're now assigning a view called post_list to the ^$ URL
#This regular expression will match ^ (a beginning) followed by $ (an end) – so only an empty string will match
