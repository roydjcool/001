from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static
from store.controller import authview

urlpatterns = [
    path('',views.home, name="home"),
    path('home',views.home, name="home"),
    path('collections', views.collections, name="collections"),
    path('collections/<str:slug>', views.collectionsview, name="collectionsview"),
    path('collections/<str:cate_slug>/<str:prod_slug>', views.productview, name="productview"),
    path('mens', views.mens, name="mens"),
    path('kids', views.kids, name="kids"),
    path('womens', views.womens, name="womens"),

    path('register', authview.register, name="register" ),
    path('login', authview.loginpage, name="loginpage" ),
    path('logout', authview.logoutpage, name="logoutpage"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)