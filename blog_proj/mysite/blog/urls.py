from django.conf.urls import url
from blog import views

urlptterns = [
    url('about/$',views.AboutView.as_view(),name='about'),
]

