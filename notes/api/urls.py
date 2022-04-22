from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from api.views import NoteViewSet, NoteImageViewSet

app_name = 'api'

router = DefaultRouter()

router.register('note', NoteViewSet, basename='note')
router.register(
    r'note/(?P<note_id>\d+)/images',
    NoteImageViewSet,
    basename='images'
)

urlpatterns = [
    path('v1/',
         include(router.urls),
         name='api_v1'),
    path('v1/api-token-auth/',
         views.obtain_auth_token,
         name='auth_token')
]
