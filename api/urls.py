from django.urls import path, include
from .views import BookViewSet, ReviewViewSet, ReadingStatusViewSet, UserListView, RegisterView, ProfileView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('books/', BookViewSet)
router.register('review/', ReviewViewSet)
router.register('readingstatus/', ReadingStatusViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('users/', UserListView.as_view(), name='users'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile')
]