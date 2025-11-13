from django.urls import include, re_path
from questions.views import IndexView


urlpatterns = [
    re_path('^', IndexView.as_view(), name='index_view'),
]
