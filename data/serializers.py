
from django.utils import timezone
from datetime import timedelta

from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.password_validation import validate_password
from django.core import exceptions as django_exceptions
from django.db import IntegrityError, transaction

from rest_framework import exceptions, serializers, status, generics


from .models import *


class FaqSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faq
        fields = '__all__'
class ProductFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductFeature
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    features = ProductFeatureSerializer(many=True,required=False,read_only=True)
    class Meta:
        model = Product
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, required=False, read_only=True)
    class Meta:
        model = Category
        fields = '__all__'


class ModelTabSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelTab
        fields = '__all__'

class ModelImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelImage
        fields = '__all__'

class ModelFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelFeature
        fields = '__all__'


class ModelSerializer(serializers.ModelSerializer):
    tabs = ModelTabSerializer(many=True,required=False,read_only=True)
    images = ModelImageSerializer(many=True,required=False,read_only=True)
    categories = CategorySerializer(many=True,required=False,read_only=True)
    technical_data = ModelFeatureSerializer(many=True,required=False,read_only=True)
    class Meta:
        model = Model
        fields = '__all__'









