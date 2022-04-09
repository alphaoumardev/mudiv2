# Create your views here.
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import viewsets
from .serializers import *
from .models import *
from rest_framework.pagination import PageNumberPagination
from django.core.paginator import Paginator


class MyPageNumberPagination(PageNumberPagination):
    page_size = 8  # default page size
    page_size_query_param = 'size'  # ?page=xx&size=??

    def get_paginated_response(self, data):
        return Response({
            'page_size': self.page_size,
            'current_page_number': self.page.number,
            'total_pages': self.page.paginator.num_pages,
            'total_products': self.page.paginator.count,
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'results': data,
        })


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by("id")
    serializer_class = ProductsModel
    pagination_class = MyPageNumberPagination
    permission_classes=[AllowAny]


# Here are just for the products
@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def get_products(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductsModel(products, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        seriliazer = ProductsModel(data=request.data)
        if seriliazer.is_valid():
            seriliazer.save()
            return Response(seriliazer.data)
        return Response(seriliazer.errors)


@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def get_product(request):
    if request.method == 'GET':
        products = Product.objects.all().order_by("id")
        pag = Paginator(object_list=products, per_page=8)
        pages = request.GET.get('page')
        result = pag.get_page(pages)
        serializer = ProductsModel(result, many=True)
        return Response(serializer.data, )
    if request.method == 'POST':
        seriliazer = ProductsModel(data=request.data)
        if seriliazer.is_valid():
            seriliazer.save()
            return Response(seriliazer.data)
        return Response(seriliazer.errors, )


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([AllowAny])
def get_one_product(request, pk):
    if request.method == "GET":
        article = Product.objects.get(id=pk)
        seriliazer = ProductsModel(article, many=False)
        return Response(seriliazer.data)
    if request.method == 'PUT':
        article = Product.objects.get(id=pk)
        seriliazer = ProductsModel(instance=article, data=request.data)
        if seriliazer.is_valid():
            seriliazer.save()
        return Response(seriliazer.data)
    if request.method == 'DELETE':
        article = Product.objects.get(id=pk)
        article.delete()
        return Response("The note is deleted")


@api_view(["GET"])
@permission_classes([AllowAny])
def get_pro_by_category(request, pk):
    if request.method == "GET":
        category = Category.objects.get(id=pk)
        variant = Product.objects.filter(category=category).order_by('-id')
        serializer = ProductsModel(variant, many=True)
        return Response(serializer.data)


@api_view(["GET"])
@permission_classes([AllowAny])
def get_genre(request):
    if request.method == "GET":
        genres = Genre.objects.all()
        serializer = GenreModel(genres, many=True)
        return Response(serializer.data)


@api_view(["GET"])
@permission_classes([AllowAny])
def get_one_genre(request, pk):
    if request.method == "GET":
        genres = Genre.objects.get(id=pk)
        serializer = GenreModel(genres, many=False)
        return Response(serializer.data)


@api_view(["GET"])
@permission_classes([AllowAny])
def get_types(request):
    if request.method == "GET":
        types = Types.objects.all()
        serializer = TypesModel(types, many=True)
        return Response(serializer.data)


@api_view(["GET"])
@permission_classes([AllowAny])
def get_one_type(request, pk):
    if request.method == "GET":
        types = Types.objects.get(id=pk)
        serializer = TypesModel(types, many=False)
        return Response(serializer.data)


@api_view(["GET"])
@permission_classes([AllowAny])
def get_category(request):
    if request.method == "GET":
        categories = Category.objects.all()
        serializer = CategoryModel(categories, many=True)
        return Response(serializer.data)


@api_view(["GET"])
@permission_classes([AllowAny])
def get_one_category(request, pk):
    if request.method == "GET":
        categories = Category.objects.get(id=pk)
        serializer = CategoryModel(categories, many=False)
        return Response(serializer.data)


@api_view(["GET"])
@permission_classes([AllowAny])
def get_by_genre(request, pk):
    if request.method == "GET":
        categories = Category.objects.filter(genre__id=pk)
        serializer = CategoryModel(categories, many=True)
        return Response(serializer.data)


@api_view(["GET"])
@permission_classes([AllowAny])
def get_by_type(request, pk):
    if request.method == "GET":
        categories = Category.objects.filter(type__id=pk)
        serializer = CategoryModel(categories, many=True)
        return Response(serializer.data)


@api_view(["GET"])
@permission_classes([AllowAny])
def get_variants(request):
    if request.method == "GET":
        variant = Variant.objects.all()
        serializer = VariantModel(variant, many=True)
        return Response(serializer.data)


@api_view(["GET"])
@permission_classes([AllowAny])
def get_one_variant(request, pk):
    if request.method == "GET":
        variant = Variant.objects.filter(product__id=pk)
        serializer = VariantModel(variant, many=True)
        return Response(serializer.data)


@api_view(["GET"])
@permission_classes([AllowAny])
def get_futured_images(request, pk):
    if request.method == "GET":
        images = FuturedImages.objects.filter(product__id=pk)
        serializer = FuturedImagesModel(images, many=True)
        return Response(serializer.data)


@api_view(["GET"])
@permission_classes([AllowAny])
def get_categories(request):
    if request.method == "GET":
        genres = Genre.objects.all()
        serializer = GenreModel(genres, many=True)
        return Response(serializer.data)


@api_view(["GET"])
@permission_classes([AllowAny])
def get_category_by_name(request, query=None):
    if request.method == "GET":
        category = Category.objects.filter(genre__genre_name=query)
        serializer = CategoryModel(category, many=True)
        return Response(serializer.data)


@api_view(["GET", "POST"])
@permission_classes([AllowAny])
def get_product_by_category(request, query=None, name=None):
    if request.method == "GET":
        genre = Category.objects.filter(genre__genre_name=query).filter(type__type_name=name)
        items = Product.objects.filter(category__genre__category__in=genre).filter(category__type__category__in=genre)
        serializer = ProductsModel(items, many=True)
        return Response(serializer.data)


@api_view(["GET"])
@permission_classes([AllowAny])
def get_sliders(request):
    if request.method == "GET":
        slide = Sliders.objects.all().order_by("-id")
        items = SlidersModel(slide, many=True)
        return Response(items.data)


@api_view(["GET"])
@permission_classes([AllowAny])
def get_new_products(request):
    if request.method == "GET":
        new_products = Product.objects.filter(onsale='New')
        items = ProductsModel(new_products, many=True)
        return Response(items.data)


@api_view(["GET"])
@permission_classes([AllowAny])
def get_onsale_products(request):
    if request.method == "GET":
        new_products = Product.objects.filter(onsale='Sale')
        items = ProductsModel(new_products, many=True)
        return Response(items.data)


@api_view(["GET"])
@permission_classes([AllowAny])
def get_colors(request):
    if request.method == "GET":
        colors = ColorsOption.objects.all()
        items = ColorsOptionModel(colors, many=True)
        return Response(items.data)


@api_view(["GET"])
@permission_classes([AllowAny])
def get_sizes(request):
    if request.method == "GET":
        sizes = SizesOption.objects.all()
        items = SizesOptionModel(sizes, many=True)
        return Response(items.data)


@api_view(["GET"])
@permission_classes([AllowAny])
def get_tags(request):
    if request.method == "GET":
        tags = Tags.objects.all()
        items = TagModel(tags, many=True)
        return Response(items.data)