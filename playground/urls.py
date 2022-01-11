from django.urls import path
from .views import PlayGroundEquipCreateView,PlayGroundEquipDeleteVIew, PlayGroundEquipDetailView,PlayGroundEquipListView,PlayGroundEquipUpdateView


urlpatterns = [
    path('',PlayGroundEquipListView.as_view(),name='play_ground_equip_list'),
    path('<int:pk>/',PlayGroundEquipDetailView.as_view(),name='play_ground_equip_detail'),
    path('create/',PlayGroundEquipCreateView.as_view(),name='play_ground_equip_create'),
    path('<int:pk>/update/',PlayGroundEquipUpdateView.as_view(),name='play_ground_equip_update'),
    path('<int>:pk>/delete/',PlayGroundEquipDeleteVIew.as_view(),name='play_ground_equip_delete')

]