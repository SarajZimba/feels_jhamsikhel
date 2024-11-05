from .views import TimedDiscountList,TimedDiscountDetail,TimedDiscountCreate,TimedDiscountUpdate,TimedDiscountDelete
from django.urls import path
urlpatterns = [
path('timeddiscount/', TimedDiscountList.as_view(), name='timeddiscount_list'),
# path('export_branch_stock/', export_branch_stock, name='export_branch_stock'),
path('timeddiscount/<int:pk>/', TimedDiscountDetail.as_view(), name='timeddiscount_detail'),
path('timeddiscount/create/', TimedDiscountCreate.as_view(), name='timeddiscount_create'),
path('timeddiscount/<int:pk>/update/', TimedDiscountUpdate.as_view(), name='timeddiscount_update'),
path('timeddiscount/delete', TimedDiscountDelete.as_view(), name='timeddiscount_delete'),
]


from .views import DiscountTableList,DiscountTableDetail,DiscountTableCreate,DiscountTableUpdate,DiscountTableDelete


urlpatterns += [
    path('discount/', DiscountTableList.as_view(), name='discounttable_list'),
    path('discount/<int:pk>/', DiscountTableDetail.as_view(), name='discounttable_detail'),
    path('discount/create/', DiscountTableCreate.as_view(), name='discounttable_create'),
    path('discount/<int:pk>/update/', DiscountTableUpdate.as_view(), name='discounttable_update'),
    path('discount/delete', DiscountTableDelete.as_view(), name='discounttable_delete'),
]
   