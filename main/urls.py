from django.conf.urls import url

from main.views import MainPageView

urlpatterns = [
  #url(r'^$', index, name = "index"),
  url(r'^$', MainPageView.as_view(), name = "index"),
]
