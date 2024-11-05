from django.urls import path
from api.views.menu import MenuCreateAPIView, MenuTypeProducts, ImageByteView, MenuListView, MenuTypeWiseListView, MenuSearchAPIView, MenuDetailView, MenuListViewAllOutlet

urlpatterns = [
    path("scanpay/menu-create/<str:outlet_name>", MenuCreateAPIView.as_view(), name="menu-create"),
    path("scanpay/menu-list/<str:outlet_name>", MenuListView.as_view(), name="menu-list"), 
    path("scanpay/menu-list-alloutlet/", MenuListViewAllOutlet.as_view(), name="menu-list-alloutlet"), 
    path("scanpay/menu-typewise-list/<str:outlet_name>", MenuTypeWiseListView.as_view(), name="menu-typewise-list"), 
    path("scanpay/menu-type-products/<str:outlet_name>/<int:id>", MenuTypeProducts.as_view(), name="menu-type-products"),
    path("scanpay/images/<str:menu_name>", ImageByteView.as_view(), name="menu-imagebyte"),
    path("scanpay/menu-detail/<int:menu_id>", MenuDetailView.as_view(), name="menu-detail"),

]

urlpatterns += [
    path("scanpay/menu-search/", MenuSearchAPIView.as_view(), name="menu-search"),

]

from api.views.menu import MenuPromotionalUpdateAPIView, MenuTodaySpecialUpdateAPIView
urlpatterns += [
    path("scanpay/update-todayspecial/<str:outlet_name>", MenuTodaySpecialUpdateAPIView.as_view(), name="update-todayspecial"),
    path("scanpay/update-promotional/<str:outlet_name>", MenuPromotionalUpdateAPIView.as_view(), name="update-promotional"),

]

from django.urls import path
from api.views.menu import FlagMenuToggleAPIView

urlpatterns += [
    path('scanpay/flagmenu/toggle/', FlagMenuToggleAPIView.as_view(), name='flagmenu-toggle'),
]


from django.urls import path
from api.views.menu import OrderAutoAcceptView

urlpatterns += [
    path('scanpay/autoaccept-order/toggle/', OrderAutoAcceptView.as_view(), name='autoacceptorder-toggle'),
]

from api.views.menu import AcceptStatus

urlpatterns += [
    path('scanpay/autoaccept-status/', AcceptStatus.as_view(), name='autoacceptorder-status'),
]

from api.views.menu import TblRedeemProductListView

urlpatterns += [
    path('scanpay/redeemproducts/', TblRedeemProductListView.as_view(), name='redeemproduct-list'),
]

# from api.views.menu import TblRedeemProductListView, RedeemedProductsView

# urlpatterns += [
#     path('redeemproducts/', TblRedeemProductListView.as_view(), name='redeemproduct-list'),

#     path('redeemedproducts/', RedeemedProductsView.as_view(), name='redeemedproducts')
# ]

from api.views.menu import TblRedeemProductListView, RedeemedProductsView, TodayRedeemedProducts ,RemoveRedeemedProducts, RemoveAllRedeemedProducts, GetRedeemedProductsView

urlpatterns += [
    path('scanpay/redeemproducts/', TblRedeemProductListView.as_view(), name='redeemproduct-list'),

    path('scanpay/redeemedproducts/', RedeemedProductsView.as_view(), name='redeemedproducts'),

    path('scanpay/get-redeemedproducts/<str:outlet>', GetRedeemedProductsView.as_view(), name='redeemedproducts'),


    path('scanpay/today-redeemedproducts/<int:order>',TodayRedeemedProducts.as_view(), name= 'today-redeemedproducts'),

    path('scanpay/removeitem-in-redeemedproducts/<int:id>',RemoveRedeemedProducts.as_view(), name= 'remove-redeemedproducts'),

    path('scanpay/remove-allredeemedproducts/<int:order>', RemoveAllRedeemedProducts.as_view(), name='remove-allredeemedproducts' )

]

from api.views.menu import PayloadToggleAPIView

urlpatterns += [
    path('scanpay/payload/toggle/', PayloadToggleAPIView.as_view(), name='payload-toggle'),
]

from api.views.menu import CreateTimedPromoMenuView

urlpatterns += [
    path('api/create-timed-promo-menu/', CreateTimedPromoMenuView.as_view(), name='create_timed_promo_menu'),
]

from api.views.menu import DiscountToggleAPIView

urlpatterns += [
    path('scanpay/discount/toggle/', DiscountToggleAPIView.as_view(), name='discount-toggle'),
]