from django.urls import path
from . import views
from .views import interpret_dream
from . import views
from .views import chatbot_process


urlpatterns = [
    path ('',views.home, name='home'),
    path('log/', views.home, name='log'),
    path('signup/', views.signup_view, name='signup'),
    path('player/', views.player_view, name='player'),
    path('homer/',views.home_reach,name='homer'),
    path('quick/',views.quick_sleep,name='quick'),
    path('deep/',views.deep_sleep,name='deep'),
    path('inner/',views.inner_peace,name='inner'),
    path('healing/',views.healing_music,name='healing'),
    path('tales/',views.tales,name='tales'),
    path('allmusic/',views.allmusic,name='allmusic'),
    path('breathing/',views.breathing,name='breathing'),
    path('apnea/',views.apnea,name='apnea'),
    path('account/',views.account,name='account'),
    path('interpret/', views.interpret_dream, name='interpret_dream'),
    path('dream/', views.dream, name='dream'),
    path('interpret_dream/', interpret_dream, name='interpret_dream'),
    path('chatbot/', views.chatbot, name='chatbot_process')
]