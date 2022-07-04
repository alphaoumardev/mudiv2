from django.urls import path
from .views import *


urlpatterns = [
    # The product
    path('pages/', get_product, name='produc'),
    path('products/', ArticleViewSet.as_view({"get": "list"}), name='product'),

    path('all/', get_products, name='product'),
    path('one/<str:pk>', get_one_product, name='one'),
    path('probycategory/<str:pk>', get_pro_by_category, name='pro'),

    # The categories
    path('genres/', get_genre, name='genres'),
    path('genre/<str:pk>', get_one_genre, name='one_genre'),

    path('types/', get_types, name='types'),
    path('type/<str:pk>', get_one_type, name='one_type'),

    path('category/', get_category, name='cate'),
    path('category/<str:pk>', get_one_category, name='one_cate'),
    path('bygenre/<str:pk>', get_by_genre, name='bygenre'),
    path('bytype/<str:pk>', get_by_type, name='bytype'),

    # The variants
    path('variants/', get_variants, name='variants'),
    path('byvariant/<str:pk>', get_one_variant, name='byvariant'),

    path('catename/', get_categories, name='categories_list'),
    path('catename/<str:query>', get_category_by_name, name='details'),
    path('catename/<str:query>/<str:name>', get_product_by_category, name='pro'),

    path('images/<str:pk>', get_futured_images, name="images"),

    path('sliders/', get_sliders, name="sliders"),
    path('newproducts/', get_new_products, name="new_products"),
    path('onsale/', get_onsale_products, name="onsale"),

    path('colors/', get_colors, name="colors"),
    path('sizes/', get_sizes, name="sizes"),
    path('tags/', get_tags, name="tags"),
    path('search/', SearchProduct.as_view(), name="search")
]
