from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin


from .views import CategoryListView, CategoryDetailView, CategoryListView_cards

urlpatterns = [
    # Examples:
    # url(r'^$', 'newsletter.views.home', name='home'),
    url(r'^$', CategoryListView.as_view(), name='categories'),
    url(r'^categories_cards/$', CategoryListView_cards.as_view(), name='categories_cards'),
    url(r'^(?P<slug>[\w-]+)/$', CategoryDetailView.as_view(), name='category_detail'),
    #url(r'^(?P<id>\d+)', 'products.views.product_detail_view_func', name='product_detail_function'),
]

