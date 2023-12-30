from django.shortcuts import render
from django.views.generic import ListView, DetailView , CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from .models import *
from .forms import *
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404

# Create your views here.

def anasayfa(request):
    return render(request, 'anasayfa.html')

class SoruListView(ListView):
    model = Soru
    template_name = 'forumapp/soru_view.html'
    context_object_name = 'sorular'
    ordering = ['-olusturulma_zamani']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search_input = self.request.GET.get('search-area') or ""
        if search_input:
            context['sorular'] = context['sorular'].filter(baslik__icontains = search_input)
            context['search_input'] = search_input
        return context


    

class SoruDetailView(DetailView):
    model = Soru
    template_name = 'forumapp/soru_detay.html'
    context_object_name = 'sorudetay'

class SoruCreateView(LoginRequiredMixin ,CreateView):
    model = Soru
    fields = ['baslik','icerik']
    template_name = 'forumapp/soru_olustur.html'
    context_object_name = 'soruolustur'

    def form_valid(self, form):
        form.instance.kullanici = self.request.user
        return super().form_valid(form)
    
class SoruUpdateView(UserPassesTestMixin,LoginRequiredMixin, UpdateView):
    model = Soru
    fields = ['baslik','icerik']
    template_name = 'forumapp/soru_olustur.html'
    context_object_name = 'soruguncelle'

    def test_func(self):
        soru = self.get_object()
        if self.request.user == soru.kullanici:
            return True
        else:
            return False
        

class SoruDeleteView(UserPassesTestMixin,LoginRequiredMixin, DeleteView):
    model = Soru
    template_name = 'forumapp/soru_sil.html'
    context_object_name = 'sorusil'
    success_url = "/sorular/"

    def test_func(self):
        soru = self.get_object()
        if self.request.user == soru.kullanici:
            return True
        else:
            return False

    
class YorumYapView(LoginRequiredMixin ,CreateView):
    model = Yorum
    form_class = YorumForm
    template_name = 'forumapp/yorum_yap.html'

    def form_valid(self, form):
        soru_id = self.kwargs.get('pk')  
        soru = get_object_or_404(Soru, pk=soru_id)
        form.instance.soru = soru  
        form.instance.kullaniciadi = self.request.user.username  
        return super().form_valid(form)       
    success_url = reverse_lazy('forumapp:sorular')