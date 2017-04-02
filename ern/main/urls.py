from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r'^hospitals/$',views.home,name="hospitals"),
    url(r'^issue/$',views.issues_view,name="issues"),
    url(r'^issuelist/$',views.issuelist_view,name="issuelist"),
    url(r'^search/$',views.search_view,name="search"),
]