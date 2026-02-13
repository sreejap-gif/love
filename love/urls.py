
from django.urls import path
from love import views
urlpatterns = [
    
    # path('sh/',views.sh),
    # path('clr/',views.clr)
    path('', views.home, name='home'),
    path('memories/', views.memories, name='memories'),
    path('love_notes/', views.love_notes, name='love_notes'),
    path('valentine/', views.valentine, name='valentine'),
]
