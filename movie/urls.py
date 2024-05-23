from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="index_page"),
    path('info-film/<int:pk>/', InfoFilms.as_view(), name="info_film_page"),
    path('profile', user_profile, name="user_profile_page"),
    path('actor/<int:pk>/', InfoActor.as_view(), name="actor_page"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
