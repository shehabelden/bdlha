from .serilezer import *
from .models import *
from rest_framework import mixins, generics


class ProductApi(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class CategoriesApi(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
