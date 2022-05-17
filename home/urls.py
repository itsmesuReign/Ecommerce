from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name='home'),
    path("index", views.index, name='home'),
    path("search/", views.search, name='search'),
    path("all_product/", views.viewAll, name='all_product'),
    path("men/", views.men, name='men'),
    path("women/", views.women, name='women'),
    path("kids/", views.kids, name='kids'),
    path("brand/", views.brand, name='brand'),
    path("accessories/", views.accessories, name='accessories'),
    path("cart/", views.cart, name='cart'),
    path("signin/", views.signin, name='signin'),
    path("product/<str:id>", views.product, name='product'),
    path("checkout/", views.checkout, name='checkout'),
    path("signup/", views.signup, name='signup'),
    path("signout/", views.signout, name='signout'),
    path("update_item/", views.updateItem, name='update_item'),
    path("product_list/<str:brand_id>", views.brandList, name='brand_list'),
    path("accessories_list/<str:accessories_id>", views.accessoriesList, name='brand_list'),
    # path("product/", views.viewAll, name='product')
]

