import random

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.generic import DetailView
from django.shortcuts import render, redirect
from .models import Movie, Actor, UserProfile, Review
from django.contrib.auth import logout


def index(request):
    movies = Movie.objects.all()
    actors = Actor.objects.all()

    big_movie = Movie.objects.all()[60:70]

    random_movie = Movie.objects.all()[random.randint(1, 80)]

    new_movies = Movie.objects.order_by('-release_year')[:10]
    popular_movies = Movie.objects.order_by('-rating')[:10]
    sad_movies = Movie.objects.filter(genre__contains='драма') | \
        Movie.objects.filter(genre__contains='криминал')
    multmovies = Movie.objects.filter(genre__contains='мультфильм') | \
        Movie.objects.filter(genre__contains='аниме')

    try:
        profile_avatar = UserProfile.objects.get(user=request.user).avatar.url
    except:
        profile_avatar = False

    return render(request, "movie/index.html", {
        "movies": movies,
        "all_actors": actors,
        "big_movie": big_movie,
        "random_movie": random_movie,
        'profile_avatar': profile_avatar,

        'new_movies': new_movies,
        'popular_movies': popular_movies,
        'sad_movies': sad_movies,
        'multmovies': multmovies
    })


class InfoFilms(DetailView):
    model = Movie
    template_name = "movie/info-films.html"
    context_object_name = 'info_film'

    def get_context_data(self, **kwargs):
        context = super(InfoFilms, self).get_context_data(**kwargs)
        review = Review.objects.filter(movie=Movie.objects.get(id=self.get_object().pk))
        try:
            profile_avatar = UserProfile.objects.all()
            profile_avatar_in_block = UserProfile.objects.get(user=self.request.user).avatar.url
        except:
            profile_avatar = False
            profile_avatar_in_block = False
        context['review'] = review
        context['profile_avatar'] = profile_avatar
        context['profile_avatar_in_block'] = profile_avatar_in_block
        return context

    def post(self, request, pk):
        new_review = Review(user=self.request.user, movie=Movie.objects.get(id=self.get_object().pk), text=request.POST["review-text"])
        new_review.save()
        return redirect('info_film_page', pk=self.get_object().pk)


def user_profile(request):
    try:
        user = UserProfile.objects.get(user=request.user)
    except:
        user = False
    movie = Movie.objects.all()
    try:
        profile_avatar_in_block = UserProfile.objects.get(user=request.user).avatar.url
    except:
        profile_avatar_in_block = False

    if request.method == 'POST':
        print(request.POST, request.FILES)
        update_field = User.objects.get(username=request.user)
        update_field.username = request.POST.get('username') if request.POST.get('username') else request.user.username
        update_field.save()

        new_avatar = request.FILES.get('avatar')
        if new_avatar:
            user_profile = UserProfile.objects.get(user=request.user)
            user_profile.avatar = new_avatar
            user_profile.save()

        return redirect('user_profile_page')

    return render(request, "movie/profile.html", {"user_profile": user, "movie": movie, "profile_avatar_in_block": profile_avatar_in_block})


class InfoActor(DetailView):
    model = Actor
    template_name = "movie/actor.html"
    context_object_name = 'info_actor'

    def get_context_data(self, **kwargs):
        context = super(InfoActor, self).get_context_data(**kwargs)
        movie = Movie.objects.all()

        try:
            profile_avatar_in_block = UserProfile.objects.get(user=self.request.user).avatar.url
        except:
            profile_avatar_in_block = False
        context['profile_avatar_in_block'] = profile_avatar_in_block
        context['movie'] = movie
        return context


def user_logout(request):
    logout(request)
    return redirect('index_page')


@login_required
def toggle_favorite_movie(request, movie_id):
    user_profile = UserProfile.objects.get(user=request.user)
    movie = Movie.objects.get(id=movie_id)

    if movie in user_profile.favorite_movies.all():
        user_profile.favorite_movies.remove(movie)
        is_favorite = False
    else:
        user_profile.favorite_movies.add(movie)
        is_favorite = True

    user_profile.save()
    return JsonResponse({'is_favorite': is_favorite})