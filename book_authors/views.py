from django.shortcuts import render
from rest_framework import generics
from .models import GenreModel , AutherModel, BookModel
from .serializer import GenreSerializers , AutherSerializer, BookSerializer
from rest_framework.permissions import IsAuthenticated
from config.permission import AdminPermission, AuthorPermission, AutherUserPermissions 
# Create your views here.



# Genre Model Api

# ListApiviews
class GenreListViews(generics.ListAPIView):
    queryset = GenreModel.objects.all()
    serializer_class = GenreSerializers
    permission_classes = (IsAuthenticated,)
    
# CreateApiviews
class GenreCreateViews(generics.CreateAPIView):
    queryset = GenreModel.objects.all()
    serializer_class = GenreSerializers
    permission_classes = (AdminPermission,)




# Auther api
class AuthersListViews(generics.ListAPIView):
    queryset = AutherModel.objects.all()
    serializer_class = AutherSerializer
    permission_classes = (IsAuthenticated,)
    
    
    

class AuthersCreateViews(generics.CreateAPIView):
    queryset = AutherModel.objects.all()
    serializer_class = AutherSerializer
    permission_classes = (AuthorPermission,)

    
class AuthersUpdateViews(generics.UpdateAPIView):
    queryset = AutherModel.objects.all()
    serializer_class = AutherSerializer
    permission_classes = (AuthorPermission,)

class AuthersDeleteViews(generics.DestroyAPIView):
    queryset = AutherModel.objects.all()
    serializer_class = AutherSerializer
    permission_classes = (AuthorPermission,)
    

#  Book api

class BookListViews(generics.ListAPIView):
    queryset =  BookModel.objects.all()
    serializer_class = BookSerializer
    permission_classes = (IsAuthenticated,)
    

class BookCreateViews(generics.CreateAPIView):
    queryset = BookModel.objects.all()
    serializer_class = BookSerializer
    permission_classes = (AutherUserPermissions,)

    
class BookUpdateViews(generics.UpdateAPIView):
    queryset =  BookModel.objects.all()
    serializer_class = BookSerializer
    permission_classes = (AuthorPermission,)

class BookDeleteViews(generics.DestroyAPIView):
    queryset =  BookModel.objects.all()
    serializer_class = BookSerializer
    permission_classes = (AuthorPermission,)
