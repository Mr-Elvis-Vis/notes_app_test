from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import NoteImageViewSet, NoteViewSet

app_name = 'api'

router = DefaultRouter()

router.register('note', NoteViewSet, basename='note')
router.register(
    r'note/(?P<note_id>\d+)/images',
    NoteImageViewSet,
    basename='images'
)

urlpatterns = [
    path('',
         include(router.urls),
         name='api_v1'),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]
