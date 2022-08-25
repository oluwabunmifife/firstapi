from django.urls import path, include
# from .views import ArticleList, ArticleDetail
from rest_framework.routers import DefaultRouter
from .views import ArticleViewSet



router = DefaultRouter()
router.register('articles', ArticleViewSet, basename='articles')
# router.register('articles/<slug:slug>/', ArticleListSet, basename='Listview')


urlpatterns = [
    # path('articles/', views.article_list),
    # path('articles/<slug:slug>/', views.article_detail),
    # path('articles/', ArticleList.as_view()),
    # path('articles/<slug:slug>/', ArticleDetail.as_view()),
    path('', include(router.urls)),
]
