from django.urls import re_path
from users import views
urlpatterns = [
    re_path(r'^me/$', views.CurrentUser.as_view()),
    re_path(r'^register/$', views.Registration.as_view()),
    re_path(r'^users/$', views.UserList.as_view()),
    re_path(r'^user/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    re_path(r'^search/$', views.UserSearch.as_view()),
]