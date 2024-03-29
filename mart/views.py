# Create your views here.
from django.db.models import Q
from rest_framework import filters
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import viewsets, generics
import numpy as np

from orders.serializers import ReviewSerializer
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
    serializer_class = ProductSerializer
    pagination_class = MyPageNumberPagination
    permission_classes = [AllowAny]


# Here are just for the products
@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def get_products(request):
    if request.method == 'GET':
        # the product search
        query = request.GET.get('query') if request.GET.get('query') is not None else ''
        products = Product.objects.filter(
            Q(category__product__name__contains=query) |
            Q(category__product__name__exact=query)
        )
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        seriliazer = ProductSerializer(data=request.data)
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
        serializer = ProductSerializer(result, many=True)
        return Response(serializer.data, )
    if request.method == 'POST':
        seriliazer = ProductSerializer(data=request.data)
        if seriliazer.is_valid():
            seriliazer.save()
            return Response(seriliazer.data)
        return Response(seriliazer.errors, )


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([AllowAny])
def get_one_product(request, pk):
    if request.method == "GET":
        article = Product.objects.get(id=pk)
        reveiws = Review.objects.filter(product=article)
        count = reveiws.count()
        seriliazer = ProductSerializer(article, many=False)
        rev = ReviewSerializer(reveiws, many=True)
        return Response({"pro": seriliazer.data, "rev": rev.data, "count": count})

    if request.method == 'PUT':
        article = Product.objects.get(id=pk)
        seriliazer = ProductSerializer(instance=article, data=request.data)
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
        serializer = ProductSerializer(variant, many=True)
        return Response(serializer.data)


@api_view(["GET"])
@permission_classes([AllowAny])
def get_genre(request):
    if request.method == "GET":
        genres = Genre.objects.all()
        serializer = GenreSerializer(genres, many=True)
        return Response(serializer.data)


@api_view(["GET"])
@permission_classes([AllowAny])
def get_one_genre(request, pk):
    if request.method == "GET":
        genres = Genre.objects.get(id=pk)
        serializer = GenreSerializer(genres, many=False)
        return Response(serializer.data)


@api_view(["GET"])
@permission_classes([AllowAny])
def get_types(request):
    if request.method == "GET":
        types = Types.objects.all()
        serializer = TypeSerializer(types, many=True)
        return Response(serializer.data)


@api_view(["GET"])
@permission_classes([AllowAny])
def get_one_type(request, pk):
    if request.method == "GET":
        types = Types.objects.get(id=pk)
        serializer = TypeSerializer(types, many=False)
        return Response(serializer.data)


@api_view(["GET"])
@permission_classes([AllowAny])
def get_category(request):
    if request.method == "GET":
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)


@api_view(["GET"])
@permission_classes([AllowAny])
def get_one_category(request, pk):
    if request.method == "GET":
        categories = Category.objects.get(id=pk)
        serializer = CategorySerializer(categories, many=False)
        return Response(serializer.data)


@api_view(["GET"])
@permission_classes([AllowAny])
def get_by_genre(request, pk):
    if request.method == "GET":
        categories = Category.objects.filter(genre__id=pk)
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)


@api_view(["GET"])
@permission_classes([AllowAny])
def get_by_type(request, pk):
    if request.method == "GET":
        categories = Category.objects.filter(type__id=pk)
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)


@api_view(["GET"])
@permission_classes([AllowAny])
def get_variants(request):
    if request.method == "GET":
        variant = Variant.objects.all()
        serializer = VariantSerializer(variant, many=True)
        return Response(serializer.data)


@api_view(["GET"])
@permission_classes([AllowAny])
def get_one_variant(request, pk):
    if request.method == "GET":
        variant = Variant.objects.filter(product__id=pk)
        serializer = VariantSerializer(variant, many=True)
        return Response(serializer.data)


@api_view(["GET"])
@permission_classes([AllowAny])
def get_futured_images(request, pk):
    if request.method == "GET":
        images = FuturedImages.objects.filter(product__id=pk)
        serializer = FuturedImagesSerializer(images, many=True)
        return Response(serializer.data)


@api_view(["GET"])
@permission_classes([AllowAny])
def get_categories(request):
    if request.method == "GET":
        genres = Genre.objects.all()
        serializer = GenreSerializer(genres, many=True)
        return Response(serializer.data)


@api_view(["GET"])
@permission_classes([AllowAny])
def get_category_by_name(request, query=None):
    if request.method == "GET":
        category = Category.objects.filter(genre__genre_name=query)
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data)


@api_view(["GET", "POST"])
@permission_classes([AllowAny])
def get_product_by_category(request, query=None, name=None):
    if request.method == "GET":
        genre = Category.objects.filter(genre__genre_name=query).filter(type__type_name=name)
        items = Product.objects.filter(category__genre__category__in=genre).filter(category__type__category__in=genre)
        serializer = ProductSerializer(items, many=True)
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
        items = ProductSerializer(new_products, many=True)
        return Response(items.data)


@api_view(["GET"])
@permission_classes([AllowAny])
def get_onsale_products(request):
    if request.method == "GET":
        new_products = Product.objects.filter(onsale='Sale')
        items = ProductSerializer(new_products, many=True)
        return Response(items.data)


@api_view(["GET"])
@permission_classes([AllowAny])
def get_colors(request):
    if request.method == "GET":
        colors = ColorsOption.objects.all()
        items = ColorsOptionSerializer(colors, many=True)
        return Response(items.data)


@api_view(["GET"])
@permission_classes([AllowAny])
def get_sizes(request):
    if request.method == "GET":
        sizes = SizesOption.objects.all()
        items = SizeSerialiser(sizes, many=True)
        return Response(items.data)


@api_view(["GET"])
@permission_classes([AllowAny])
def get_tags(request):
    if request.method == "GET":
        tags = Tags.objects.all()
        items = TagSerializer(tags, many=True)
        return Response(items.data)


# Filter by color
@api_view(["GET"])
@permission_classes([AllowAny])
def filter_by_color(request):
    if request.method == "GET":
        color = request.GET.get('color') if request.GET.get('color') is not None else ''
        products = Product.objects.filter(Q(futuredimages__color_name__color_name=color))
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


# Filter product by size
@api_view(["GET"])
@permission_classes([AllowAny])
def filter_by_size(request):
    if request.method == "GET":
        size = request.GET.get('size') if request.GET.get('size') is not None else ''
        products = Product.objects.filter(Q(variant__size__size_name=size))
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


# Filter product by Tags
@api_view(["GET"])
@permission_classes([AllowAny])
def filter_by_tag(request):
    if request.method == "GET":
        tag = request.GET.get('tag') if request.GET.get('tag') is not None else ''
        products = Product.objects.filter(Q(variant__tag=tag) |
                                          Q(variant__tag__tag_name=tag))
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


# Filter product by Price
@api_view(["GET"])
@permission_classes([AllowAny])
def filter_by_price(request):
    if request.method == "GET":
        less_price = request.GET.get('less_price') if request.GET.get('less_price') is not None else None
        greater_price = request.GET.get('greater_price') if request.GET.get('greater_price') is not None else None
        # price = Product.objects.get('price')
        products = Product.objects.filter(price__gte=less_price,
                                          price__lte=greater_price)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def review_products(request):
    if request.method == "POST":
        serializer = ReviewSerializer(data=request.data, many=False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    if request.method == "GET":
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)
