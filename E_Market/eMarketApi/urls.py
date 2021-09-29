from django.urls import path, include
from eMarketApi import views
from django.views.decorators.csrf import csrf_exempt
#from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'eMarketApi'

#router = routers.DefaultRouter()

#router.register(r'category', views.CategoryList)
#router.register(r'category/<pk>', views.CategoryList)

urlpatterns = [
    path('', views.CategoryList.as_view(), name = 'category_list'),
    path('categoryapi/<pk>/', views.CategoryDetail.as_view(), name = 'category-detail'),
    path('productsapi/', views.ProductList.as_view(), name = 'products_list'),
    path('usersapi/', views.UserList.as_view(), name = 'user_list'),
    path('usercreateapi/', views.UserCreate.as_view(), name = 'user_create'),
    path('usersinfoapi/', views.UserInfoList.as_view(), name = 'userinfo_list'),
    path('usersinfoapi/<pk>/', views.UserInfoDetail.as_view(), name = 'userinfo_detail'),
    path('login/', csrf_exempt(views.LoginView.as_view()), name = 'login'),
    path('logout/', csrf_exempt(views.LogoutView.as_view()), name = 'logout'),
    path('orderitemapi/', views.OrderItemList.as_view(), name = 'orderitem_list'),
    path('orderitemapi/<pk>/', views.OrderItemDetail.as_view(), name = 'orderitem-detail'),
    path('orderapi/', views.OrderList.as_view(), name = 'order_list'),
    path('orderapi/<pk>/', views.OrderDetail.as_view(), name = 'order-detail'),
    path('add-to-cart-api/<id>/', views.addToCartApi, name = 'add-to-cart-api'),
    path('remove-from-cart-api/<id>/', views.removeFromCartApi, name = 'remove-from-cart-api'),
    path('remove-single-single-item-api/<id>/', views.removeSingleItemFromCartApi, name = 'remove-single-single-item-api'),
    path('order-item-api/', views.orderItemApi, name = 'order-item-api'),
    path('address-api/', views.AddressApi.as_view(), name = 'address-api'),
    path('payment-api/', views.PaymentApi.as_view(), name = 'payment-api')
]

"""path('categoryapi/<pk>/', views.CategoryDetail.as_view(), name = 'category-detail'),
    path('productsapi/', views.ProductList.as_view(), name = 'products_list'),
    path('productsapi/<pk>/', views.ProductDetail.as_view(), name = 'products-detail'),
    path('usersapi/', views.UserList.as_view(), name = 'user_list'),
    path('usersapi/<pk>/', views.UserDetail.as_view(), name = 'user-details'),
    path('usersinfoapi/', views.UserInfoList.as_view(), name = 'userinfo_list'),
    path('login/', (views.LoginView.as_view()), name="login"),
    path('logout/', csrf_exempt(views.LogoutView.as_view()), name="logout"),
    path('orderitemapi/', views.OrderItemList.as_view(), name = 'orderitem_list'),
    path('orderitemapi/<pk>/', views.OrderItemDetail.as_view(), name = 'orderitem-detail'),
    path('orderapi/', views.OrderList.as_view(), name = 'order_list'),
    path('orderapi/<pk>/', views.OrderDetail.as_view(), name = 'order-detail'),
    path('addressapi/', views.AddressList.as_view(), name = 'address_list'),
    path('addressapi/<pk>/', views.AddressDetail.as_view(), name = 'address-detail'),
    path('paymentapi/', views.PaymentList.as_view(), name = 'payment_list'),
    path('paymentapi/<pk>/', views.PaymentDetail.as_view(), name = 'payment-detail'),
    path('userorder/', views.getUserOrderItems, name = 'user-order')"""


