from django.urls import path
from hello import views

urlpatterns = [
    path("", views.home, name="home"),
    path("hello/<name>", views.hello_there, name="hello_there"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),    
    path("send_notification/<to_num>/<notif_message>/<limit>", views.send_notification, name="send_notification"),     
]