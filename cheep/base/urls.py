from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [   
    path('', views.home),
    path('login/', views.loginPage),
    path('logout/', views.logoutPage),
    path('registro/', views.registerPage),
    path('comment/', views.comment),
    path('post/', views.post),
    path('post/<int:id>', views.post),
    path('profile/', views.profile, name='profile'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('feed/', views.feed, name='feed'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)