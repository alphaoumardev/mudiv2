from django.urls import path
from . import views

urlpatterns = [
    # The product
    path('pages/', views.get_product, name='produc'),
    path('products/', views.ArticleViewSet.as_view({"get": "list"}), name='product'),

    path('all/', views.get_products, name='product'),
    path('one/<str:pk>', views.get_one_product, name='one'),
    path('probycategory/<str:pk>', views.get_pro_by_category, name='pro'),

    # The categories
    path('genres/', views.get_genre, name='genres'),
    path('genre/<str:pk>', views.get_one_genre, name='one_genre'),

    path('types/', views.get_types, name='types'),
    path('type/<str:pk>', views.get_one_type, name='one_type'),

    path('category/', views.get_category, name='cate'),
    path('category/<str:pk>', views.get_one_category, name='one_cate'),
    path('bygenre/<str:pk>', views.get_by_genre, name='bygenre'),
    path('bytype/<str:pk>', views.get_by_type, name='bytype'),

    # The variants
    path('variants/', views.get_variants, name='variants'),
    path('byvariant/<str:pk>', views.get_one_variant, name='byvariant'),

    path('catename/', views.get_categories, name='categories_list'),
    path('catename/<str:query>', views.get_category_by_name, name='details'),
    path('catename/<str:query>/<str:name>', views.get_product_by_category, name='pro'),

    path('images/<str:pk>', views.get_futured_images, name="images"),

    path('sliders/', views.get_sliders, name="sliders"),
    path('newproducts/', views.get_new_products, name="new_products"),
    path('onsale/', views.get_onsale_products, name="onsale"),

    path('colors/', views.get_colors, name="colors"),
    path('sizes/', views.get_sizes, name="sizes"),
    path('tags/', views.get_tags, name="tags"),
]
