from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static
from store.controller import authview, cart, wishlist, checkout

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

    path('add-to-cart', cart.addtocart, name="addtocart"),
    path('cart', cart.viewcart, name="cart"),
    path('delete-cart-item', cart.deletecartitem, name="deletecartitem"),

    path('wishlist', wishlist.index, name="wishlist"),
    path('add-to-wishlist', wishlist.addtowishlist, name="addtowishlist"),
    path('delete-wishlist-item',wishlist.deletewishlistitem, name="deletewishlistitem"),

    path('checkout', checkout.index, name="checkout")
   
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)