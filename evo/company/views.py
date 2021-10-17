from django.shortcuts import render, get_object_or_404
from django.views.generic import ( ListView, DetailView, CreateView, UpdateView, DeleteView)
from django.contrib import messages
from .models import JobPlan, MarketPlan
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
 

# Create your views here.
#List view
class JobPlanListView(LoginRequiredMixin, ListView):
    model = JobPlan
    template_name = 'company/jobp_list.html'
    paginate_by = 2

    

class MarketPlanListView(LoginRequiredMixin, ListView):
    model = MarketPlan
    template_name = 'company/marketp_list.html'
    paginate_by = 2


#Detail view
class JobPlanDetailView( LoginRequiredMixin, DetailView):
    model = JobPlan
    template_name = 'company/detail_jobp.html'


class MarketPlanDetailView( LoginRequiredMixin, DetailView):
    model = MarketPlan
    template_name = 'company/detail_marketp.html'
    
    


#Create view
class JobPlanCreateView( LoginRequiredMixin, CreateView):
    model = JobPlan
    template_name = 'company/new_jobp.html'
    fields = ['name','customer', 'file_no', 'origin_port', 'destination_port', 'description', 'product', 'forwarder', 'clearing_agent','marketer', 'buying', 'selling', 'margin', 'status']
    


    def form_valid(self, form):
        form.instance.name = self.request.user
        return super().form_valid(form)




class MarketPlanCreateView( LoginRequiredMixin, CreateView):
    model = MarketPlan
    template_name = 'company/new_marketp.html'
    fields = ['name','file_ref_no', 'account_code_no', 'marketer', 'director_name', 'director_no', 'location', 'product_description', 'comodity', 'communication', 'travelling_accomodation', 'advertising', 'total', 'remarks']


    def form_valid(self, form):
        form.instance.name = self.request.user
        return super().form_valid(form)



#Update view
class JobPlanUpdateView( LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = JobPlan
    template_name = 'company/new_jobp.html'
    fields = ['name','customer', 'file_no', 'origin_port', 'destination_port', 'description', 'product', 'forwarder', 'clearing_agent','marketer', 'buying', 'selling', 'margin', 'status']
    


    def form_valid(self, form):
        form.instance.name = self.request.user
        return super().form_valid(form)


    def test_func(self):
        object = self.get_object()
        if self.request.user == object.name:
            return True
        return False


class MarketPlanUpdateView( LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = MarketPlan
    template_name = 'company/new_marketp.html'
    fields = ['name','file_ref_no', 'marketer', 'director_name', 'director_no', 'location', 'product_description', 'comodity', 'communication', 'travelling_accomodation', 'advertising', 'total', 'remarks']
    


    def form_valid(self, form):
        form.instance.name = self.request.user
        return super().form_valid(form)


    def test_func(self):
        object = self.get_object()
        if self.request.user == object.name:
            return True
        return False



#Delete view
class JobPlanDeleteView( LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = JobPlan
    template_name = 'company/delete_jobp.html'
    success_url = '/'


    def test_func(self):
        object = self.get_object()
        if self.request.user == object.name:
            return True
        return False


class MarketPlanDeleteView( LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = MarketPlan
    template_name = 'company/delete_marketp.html'
    success_url = '/'


    def test_func(self):
        object = self.get_object()
        if self.request.user == object.name:
            return True
        return False