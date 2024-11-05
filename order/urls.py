from django.urls import path
from .views import HomeView

urlpatterns = [
    path("", HomeView, name="home")
]
from .views import QrDetail, QrList
urlpatterns += [
path('qr/', QrList.as_view(), name='qr_list'),
path('qr/<int:pk>/', QrDetail.as_view(), name='qr_detail'),
# path('menu/type/create/', MenuTypeCreate.as_view(), name='menu_type_create'),
# path('menu/type/<int:pk>/update/', MenuTypeUpdate.as_view(), name='menu_type_update'),
# path('menu/type/delete', MenuTypeDelete.as_view(), name='menu_type_delete'),

]