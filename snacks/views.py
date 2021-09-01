from django.views.generic import (
    ListView,
    DetailView,
    UpdateView,
    CreateView,
    DeleteView,
)
from django.urls import reverse_lazy
from .models import Snacks


class SnackListView(ListView):
    template_name = "snack_list.html"
    model = Snacks


class SnackDetailView(DetailView):
    template_name = "snack_detail.html"
    model = Snacks


class SnackUpdateView(UpdateView):
    template_name = "snack_update.html"
    model = Snacks
    fields = ["name", "purchaser", "description"]


class SnackCreateView(CreateView):
    template_name = "snack_create.html"
    model = Snacks
    fields = ["name", "purchaser", "description"]


class SnackDeleteView(DeleteView):
    template_name = "snack_delete.html"
    model = Snacks
    success_url = reverse_lazy("snack_list")
