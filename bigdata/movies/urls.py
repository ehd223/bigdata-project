from django.urls import path, include
from . import views

app_name = 'movies'
urlpatterns = [
    path('', views.index, name='index'),
    path('login_register', views.login_register, name='login_register'),
    path('api/genres_count/<int:year>', views.genres_count, name='genres_count'),
    path('signin', views.signin, name='signin'),
    path('signout', views.signout, name='signout'),
    path('signup', views.signup, name='signup'),
    path('clublist', views.clublist, name='clublist'),
    path('clubview', views.clubview, name='clubview'),
    path('postsubmit', views.postsubmit, name='postsubmit'),
    path('commentsubmit', views.commentsubmit, name='commentsubmit'),
    path('myclub', views.myclub, name='myclub'),
    path('clubmember', views.clubmember, name='clubmember'),
    path('movielist', views.movielist, name='movielist'),
    path('movieview', views.movieview, name='movieview'),
    path('toprated', views.toprated, name='toprated'),
    path('clubrecommend', views.clubrecommend, name='clubrecommend')

    path('genrescount', views.genre_count_page, name='genrescount'),
    path('api/genrescount/<int:year>', views.genres_count, name='genrescount_api'),

    path('clubpick', views.club_pick, name='clubpick'),
    path('api/clubpick/<int:club_id>', views.club_pick_api, name='clubpick_api'),
] 
urlpatterns+=[
    path('', include('django.contrib.auth.urls')),
]