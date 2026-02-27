from django.urls import path
from .views import BookViewSet, ReviewViewSet, ReadingStatusViewSet, UserListView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('books/', BookViewSet.as_view(), name='books'),
    path('review/', ReviewViewSet.as_view(), name='review'),
    path('readingstatus/', ReadingStatusViewSet.as_view(), name='readingstatus'),
    path('users/', UserListView.as_view(), name='users'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh')
]