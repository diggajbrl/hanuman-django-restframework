from django.shortcuts import render

from rest_framework import generics
from .models import User
from .serializers import UserSerializer
# Create your views here.

def app (request) :

    if request.method=='POST' :
        user_email = request.POST.get('email')
    
        ex = User(email = user_email)
        ex.save()
    

    return render (request, 'index.html')

class UserListApiView (generics.ListCreateAPIView) :
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetails (generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer   