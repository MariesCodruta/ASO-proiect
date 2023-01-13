from django.urls import path

from . import views

urlpatterns = [

    path('aso/', views.index, name='index'),
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('', views.home, name="home"),
    path('<str:room>/', views.room, name="room"),
    path('checkview', views.checkview, name="checkview"),
    path('send', views.send, name="send"),
    path('getMessages/<str:room>/', views.getMessages, name="getMessages"),

    # # ex: /aso/5/
    # path('<int:question_id>/', views.detail, name='detail'),
    # # ex: /aso/5/results/
    # path('<int:question_id>/results/', views.results, name='results'),
    # # ex: /aso/5/vote/
    # path('<int:question_id>/vote/', views.vote, name='vote'),
    #
    # path('<int:question_id>/', views.detail, name='detail'),
    #
    # path('specifics/<int:question_id>/', views.detail, name='detail'),
]
