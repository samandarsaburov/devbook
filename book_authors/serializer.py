from rest_framework.serializers import ModelSerializer
from .models import GenreModel, AutherModel, BookModel
from django.shortcuts import get_object_or_404
from account.models import CustomUser


# Genre Serializers
class GenreSerializers(ModelSerializer):
    class Meta:
        model = GenreModel
        fields = ('name',)
        

# Auther Serializer
class AutherSerializer(ModelSerializer):
    class Meta:
        model = AutherModel
        fields = ('first_name','last_name','date_of_brth','place_of_birth','Date_of_death','Place_of_death','images','bio','genre','user')

    # def Create(self, validat_data):
        
        
    #     validat_data['user'] = get_object_or_404(CustomUser, user=self.context['request'])
    #     return super(AutherSerializer,self).create(validat_data)
    
    
    
    
    
#  Book Serializer
class BookSerializer(ModelSerializer):
    class Meta:
        model = BookModel
        fields = ('title','pages','year','price','genre','images','auther','bio','user')
