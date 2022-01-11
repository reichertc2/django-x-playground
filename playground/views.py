from django.views.generic import (ListView,DetailView,CreateView,UpdateView,DeleteView)
from django.urls import reverse_lazy
from .models import PlayGroundEquip

# Create your views here.
class PlayGroundEquipListView(ListView):
    template_name = 'play_ground_equip_list.html'
    model = PlayGroundEquip

class PlayGroundEquipDetailView(DetailView):
    template_name = 'play_ground_equip_detail.html'
    model = PlayGroundEquip

class PlayGroundEquipCreateView(CreateView):
    template_name = 'play_ground_equip_create.html'
    model = PlayGroundEquip
    fields = ['name', 'description', 'safety_rating','approved_by']

class PlayGroundEquipUpdateView(UpdateView):
    template_name = 'play_ground_equip_update.html'
    model = PlayGroundEquip
    fields = ['name', 'description', 'safety_rating','approved_by']

class PlayGroundEquipDeleteVIew(DetailView):
    template_name = 'play_ground_equip_delete.html'
    model = PlayGroundEquip
    success_url = reverse_lazy('play_ground_equip_list')
