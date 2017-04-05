from django.http.response import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView, UpdateView

from main.models import Investor


class InvestorList(ListView):
    model = Investor


def process_children(node, sum):
    node.sum += sum / 100 * node.percent
    node.save()
    for children in node.get_children():
        process_children(children, sum)


def process_parent(node, sum):
    node.sum += sum / 100 * node.percent
    node.save()
    if node.parent:
        process_parent(node.parent, sum)


def add_sum(request, *args, **kwargs):
    node = Investor.objects.get(pk=kwargs['pk'])
    node.sum += float(request.GET['sum'])
    node.save()

    if node.parent:
        process_parent(node.parent, float(request.GET['sum']))

    return HttpResponseRedirect(reverse('investor_list'))