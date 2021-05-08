from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("one/", views.one),
    path("two/", views.two),
    path("three/", views.three),
    path("four/", views.four),
    path("five/", views.five),
    path("six/", views.six),
    path("seven/", views.seven),
    path("eight/", views.eight),
    path("nine/", views.nine),
    path("ten/", views.ten),

]