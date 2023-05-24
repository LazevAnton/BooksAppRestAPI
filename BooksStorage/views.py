from rest_framework.viewsets import ModelViewSet

from BooksStorage.models import BooksInfo
from BooksStorage.serializer import BooksSerializer


class BooksViewSet(ModelViewSet):
    queryset = BooksInfo.objects.all()
    serializer_class = BooksSerializer
