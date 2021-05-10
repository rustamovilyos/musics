# from django.urls import path
#
# from . import views
#
# urlpatterns = [
#     path("", views.index, name="index"),
#     path("one/", views.one),
#     path("two/", views.two),
#     path("three/", views.three),
#     path("four/", views.four),
#     path("five/", views.five),
#     path("six/", views.six),
#     path("seven/", views.seven),
#     path("eight/", views.eight),
#     path("nine/", views.nine),
#     path("ten/", views.ten),
#
# ]

from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('', views.index, name='index'),
]