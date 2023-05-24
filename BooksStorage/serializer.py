from rest_framework.serializers import ModelSerializer
from BooksStorage.models import BooksInfo


class BooksSerializer(ModelSerializer):
    class Meta:
        model = BooksInfo
        fields = '__all__'
