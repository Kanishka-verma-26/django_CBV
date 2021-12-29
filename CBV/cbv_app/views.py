from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (View, TemplateView,
                                  ListView, DetailView,
                                  CreateView, UpdateView, DeleteView)
from django.http import HttpResponse
from . import models

# Create your views here.


# # function based view
# def indexx(request):
#     return render(request,'indexx.html')
#
# # basic class based view
# class CBView(View):
#     def get(self,request):
#         return HttpResponse("CLASS BASED VIEWS ARE COOL")
#
#
# class based template view
class IndexView(TemplateView):
    template_name = 'indexx.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['injectme'] = 'Basic Injection!!!'
        return context


class SchoolListView(ListView):
    # school_list is the default context_object_name created when we passed model = models.School in ListView
    # ListView returns 'modelname.lower()'+'_list' = 'school_list'
    # either we can pass 'school_list' or we can define another name using context_object_name
    context_object_name = 'schools'
    model = models.School


class SchoolDetailView(DetailView):
    # DetailView returns 'modelname.lower()' = 'school'
    # either we can pass 'school' or we can define another name using context_object_name
    context_object_name = 'school_detail'
    model = models.School
    template_name = 'cbv_app/school_details.html'

class SchoolCreateView(CreateView):
    # CreateView returns 'modelname.lower()' = 'school'
    fields = ('name','principle','location')
    model = models.School

class SchoolUpdateView(UpdateView):
    # UpdateView returns 'modelname.lower()' = 'school'

    fields = ('name','principle')
    model = models.School

class SchoolDeleteView(DeleteView):
    # DeleteView returns 'modelname.lower()' = 'school'

    # Class Based Views automatically setup everything
    # from A to Z. One just needs to specify which model to
    # create DeleteView for, then Class based DeleteViewde will
    # automatically try to find a template in app_name/modelname_confirm_delete.html.
    # In our case it is school_confirm_delete.html,
    # but we created the template with "school_dlt_confirm.html" name instead of "school_confirm_delete.html".
    # hence we redefined the template_name

    model = models.School
    template_name = "cbv_app/school_dlt_confirm.html"
    success_url = reverse_lazy("cbv_app:list")