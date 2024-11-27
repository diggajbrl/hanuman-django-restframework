from django.urls import path
from .views import app, UserListApiView, UserDetails

urlpatterns = [
    path('', app, name='app'),
    path('api/users/', UserListApiView.as_view(), name='user-list'),
    path('api/users/<int:pk>/', UserDetails.as_view(), name='user-details'),
]