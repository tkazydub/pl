from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from .models import CheckList,ListItem,ListItemDescription
from django.views import generic
from product_list.forms import ListItemForm
from django.core.urlresolvers import reverse
from django.template.response import TemplateResponse

# Create your views here.
class IndexView(generic.ListView):
    template_name = "product_list/index.html"
    context_object_name = "latest_lists"

    def get_queryset(self):
        return CheckList.objects.all()

class DetailView(generic.DetailView):
    model = CheckList
    template_name = "product_list/list_detail.html"

class ShowItemsView(generic.ListView):
    model = ListItemDescription
    template_name = "product_list/items.html"


def add_new_list(request):
    return TemplateResponse(request,'product_list/add_new_list.html', {}).render()

def add_new_item(request):
    return TemplateResponse(request,'product_list/register_item.html', {}).render()

class AddCustomItemView(generic.DetailView):
    model = CheckList
    template_name = 'product_list/add_custom_item.html'

def save_item_to_list(request, item_id):
    check_list = CheckList.objects.get(id=item_id)
    if request.method == 'POST':
        check_list.listitem_set.create(name=request.POST.get('name', ''), status=request.POST.get('status', ''))
    return HttpResponseRedirect(reverse('product_list:detail',kwargs={'pk': item_id}))

def remove_item_from_list(request, list_id, item_id):
    item = CheckList.objects.get(id=list_id).listitem_set.get(id=item_id)
    item.delete()
    return HttpResponseRedirect(reverse('product_list:detail',kwargs={'pk': list_id}))

def remove_item(request, item_id):
    item = ListItemDescription.objects.get(id=item_id)
    item.delete()
    return HttpResponseRedirect(reverse('product_list:items'))

def update_item(request, item_id):
    item = ListItemDescription.objects.get(id=item_id)
    if request.method == 'POST':
        item.name = request.POST.get('name','')
        item.description = request.POST.get('description','')
        item.quantity = request.POST.get('quantity','')
        item.quantity_units = request.POST.get('quantity_units','')
        item.status = request.POST.get('status','')
        item.save()
    return HttpResponseRedirect(reverse('product_list:items'))

class EditItemView(generic.DetailView):
    model = ListItemDescription
    template_name = "product_list/edit_item.html"


def save_item(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        description = request.POST.get('description', '')
        quantity = request.POST.get('quantity', '')
        quantity_units = request.POST.get('quantity_units','')
        status = request.POST.get('status','')
        ListItemDescription(name=name,description=description,quantity=quantity,quantity_units=quantity_units,status=status).save()


    return HttpResponseRedirect(reverse('product_list:items'))


class LinkItemDescView(generic.ListView):
    template_name = "product_list/link_item_desc.html"
    context_object_name = 'desc_list'
    queryset = ListItemDescription.objects.all()
    def get_context_data(self, **kwargs):
        context = super(LinkItemDescView, self).get_context_data(**kwargs)
        context['item_id'] = self.kwargs['item_id']
        context['list_id'] = self.kwargs['list_id']
        context['item_name'] = ListItem.objects.get(id=self.kwargs['item_id'])
        return context


def desc_list_link(request, list_id, item_id, desc_id):
    description = ListItemDescription.objects.get(id=desc_id)
    ListItem.objects.get(id=item_id).itemtoitemdescription_set.create(item_description_id=description)
    return HttpResponseRedirect(reverse('product_list:detail',kwargs={'pk': list_id}))

def add_list(request):
    if request.method == 'POST':
        title = request.POST.get('title', '')
        status = request.POST.get('status', '')
        CheckList(title=title,status=status).save()
    return HttpResponseRedirect(reverse('product_list:index'))

def DetailedView(request,list_id):
    print "list id: ",list_id
    list = get_object_or_404(CheckList,pk=list_id)
    output = ", ".join([p.name for p in list.listitem_set.all()])
    return HttpResponse(output)