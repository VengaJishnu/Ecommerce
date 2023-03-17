from django.urls import path
from . import views
app_name='ecommerce'
urlpatterns = [
    path('',views.allproducts,name='allproducts'),
    path('<slug:c_slug>/',views.allproducts,name='products_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/',views.proDetail,name='proCatdetail'),
]
