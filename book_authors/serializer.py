from rest_framework.serializers import ModelSerializer
from .models import GenreModel, AutherModel, BookModel
from django.shortcuts import get_object_or_404
from account.models import CustomUser



# Genre Serializers
class GenreSerializers(ModelSerializer):
    class Meta:
        model = GenreModel
        fields = ('id','name')
        

# Auther Serializer

class AutherSerializer(ModelSerializer):
    class Meta:
        model = AutherModel
        fields = ('id','first_name','last_name','date_of_brth','place_of_birth','date_of_death','place_of_death','images','bio','genre')

    # def create(self, validated_data):
    #     # print(self.context['request'].user.id)
    #     validated_data['user'] = CustomUser.objects.get(user=self.context['request'].user)
    #     return super(AutherSerializer, self).create(validated_data)
    

#  Book Serializer
class BookSerializer(ModelSerializer):
    class Meta:
        model = BookModel
        fields = ('title','pages','year','price','genre','images','auther','bio','user')
    
    
    # def create(self, validated_data):
    #     validated_data['auther'] = get_object_or_404(AutherModel, user=self.context['request'])
    #     return super(BookSerializer,self).create(validated_data)
