from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Avg
from django.contrib.auth.mixins import LoginRequiredMixin


from .models import Movie, Review

class MovieListView(ListView):
    model = Movie
    template_name = 'movie_list.html'

    def get_queryset(self):
        queryset = Movie.objects.all()

        search = self.request.GET.get('q')
        genre = self.request.GET.get('genre')

        if search:
            queryset = queryset.filter(title__icontains=search)

        if genre:
            queryset = queryset.filter(genre__name=genre)


        queryset = queryset.annotate(avg_rating=Avg('reviews__mark')).order_by('-avg_rating')

  
    
class MovieDetailView(DetailView):
    model = Movie
    template_name = 'movie_detail.html'

class MovieCreateView(LoginRequiredMixin, CreateView):
    model = Movie
    fields = '__all__'
    template_name = 'movie_form.html'
    success_url = reverse_lazy('movie_list')

class MovieUpdateView(LoginRequiredMixin, UpdateView):
    model = Movie
    fields = '__all__'
    template_name = 'movie_form.html'
    success_url = reverse_lazy('movie_list')

class MovieDeleteView(LoginRequiredMixin, DeleteView):
    model = Movie
    template_name = 'movie_confirm_delete.html'
    success_url = reverse_lazy('movie_list')

class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = Review
    fields = ['mark', 'text']

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.movie_id = self.kwargs['pk']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('movie_detail', kwargs={'pk': self.kwargs['pk']})
