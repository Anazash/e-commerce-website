from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login1/', views.login1, name='login1'),
    path('login/', views.login, name='login'),
    path('signup/',views.signup,name='signup'),
    path('add_category/',views.add_category,name="add_category"),
    path('add_product/', views.add_product, name='add_product'),
    path('add_products/', views.add_products, name='add_products'),
    path('show_product/', views.show_product, name='show_product'),
    path('new_arrivals/', views.new_arrivals, name='new_arrivals'),
    path('add-to-cart/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart, name='cart'),
    path('new/',views.new,name='new'),
    path('adp/',views.adp,name='adp'),
    path('shpd/',views.shpd,name='shpd'),
    path('shus/',views.shus,name='shus'),
    path('adct/',views.adct,name='adct'),
    path('show_user/', views.show_user, name='show_user'),
    # path('edit_student/<int:pk>/', views.edit_student, name='edit_student'),
    path('delete_product/<int:id>/', views.delete_product, name='delete_product'),
    path('admin1',views.admin1,name='admin1'),
    path('user_signup',views.user_signup,name='user_signup'),
    path('add_user',views.add_user,name='add_user'),
    # path('teach',views.teach,name='teach'),
    # path('see_pro',views.see_pro,name='see_pro'),
    # path('edit_teach',views.edit_teach,name='edit_teach'),
    path('logout/',views.logout,name="logout"),
    

]

