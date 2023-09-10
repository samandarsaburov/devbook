from django.db import models
from account.models import CustomUser
# Create your models here.


#  Genre Model
class GenreModel(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self) -> str:
        return self.name
    class Meta:
        db_table = 'genre'
    

# Auther models ss
class AutherModel(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    date_of_brth = models.DateField(null= True, blank=True)
    place_of_birth = models.CharField(max_length=50,default='')
    date_of_death = models.DateField(null=True, blank=True)
    place_of_death = models.CharField(max_length=50, default='')
    images = models.ImageField(upload_to='auther/',blank=True, null=True)
    bio = models.TextField(default='')
    genre =models.ForeignKey(GenreModel,on_delete=models.CASCADE,default='')
    user = models.ForeignKey(CustomUser,on_delete = models.CASCADE, default= 2)
    def __str__(self) -> str:
        return self.first_name    
    class Meta:
        db_table = 'auther'
        
        
# book model ss
class BookModel(models.Model):
    title = models.CharField(max_length=25)
    pages = models.IntegerField()
    year = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    images = models.ImageField(upload_to='book/',blank=True, null=True)
    bio = models.TextField()
    auther = models.ForeignKey(AutherModel, on_delete=models.CASCADE,default= '')
    genre =models.ForeignKey(GenreModel,on_delete=models.CASCADE,default='')
    user = models.ForeignKey(CustomUser,on_delete = models.CASCADE, default=2)
    def __str__(self) -> str:
        return self.title
    class Meta:
        db_table = 'book'