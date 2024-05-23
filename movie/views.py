import random
from django.views.generic import DetailView
from django.shortcuts import render
from .models import Movie, Actor, UserProfile, Review


def index(request):
    movies = Movie.objects.all()
    actors = Actor.objects.all()

    big_movie = Movie.objects.all()[60:70]

    random_movie = Movie.objects.all()[random.randint(1, 80)]
    return render(request, "movie/index.html", {
        "movies": movies,
        "all_actors": actors,
        "big_movie": big_movie,
        "random_movie": random_movie
    })


class InfoFilms(DetailView):
    model = Movie
    template_name = "movie/info-films.html"
    context_object_name = 'info_film'

    def get_context_data(self, **kwargs):
        context = super(InfoFilms, self).get_context_data(**kwargs)
        review = Review.objects.filter(user=self.request.user)
        profile_avatar = UserProfile.objects.get(user=self.request.user).avatar.url
        context['review'] = review
        context['profile_avatar'] = profile_avatar
        return context


def user_profile(request):
    user = UserProfile.objects.get(user=request.user)
    movie = Movie.objects.all()
    return render(request, "movie/profile.html", {"user_profile": user, "movie": movie})


class InfoActor(DetailView):
    model = Actor
    template_name = "movie/actor.html"
    context_object_name = 'info_actor'

    def get_context_data(self, **kwargs):
        context = super(InfoActor, self).get_context_data(**kwargs)
        movie = Movie.objects.all()
        context['movie'] = movie
        return context
