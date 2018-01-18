from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('chat', views.chat, name='chat'),
    path('del_msgs', views.delete_messages),
    re_path(r'new_msg/$', views.get_msg)
]
