from rest_framework import serializers
from .models import Product, Category, Comment, Vote, Profile, Fetched_Product
from django.contrib.auth.models import User
from rest_framework.authtoken.views import Token

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["name"]


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=True)
    class Meta:
        model = Product
        fields = ( 
            "id",
            "bggid",
            "name",
            "slug",            
            "description",            
            "is_active",  
            "category",
            "min_players",        
            "max_players",    
            "image1",   
            "image2",   
            "image3",   
            "image4",   
            "image5",   
            "thumbnail",            
        )


class Fetched_ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=True)
    class Meta:
        model = Fetched_Product
        fields = ( 
            "id",
            "bggid",
            "name",
            "slug", 
            "description",  
            "category", 
            'min_players',
            'max_players',    
            "image_url",
            'thumbnail_url'            
        )

        
class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Comment
        fields = ["id","product","body","created_on","owner"]


class VoteSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Vote


        fields = ["id","product","value","owner"]

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'username','password']

        extra_kwargs = {'password':{
            'write_only':True,
            'required':True
        }}
    def create(self, validated_data):
        user=User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user