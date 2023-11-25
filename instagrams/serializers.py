from .models import Post
from rest_framework.serializers import ModelSerializer

class PostBaseModelSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'