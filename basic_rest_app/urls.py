from django.urls import path, include
from . import views

urlpatterns = [
    # path('', views.index, name="index"),
    path('', views.classBasedIndex.as_view(), name="index"),
    path('detail/<int:pk>', views.ArticleDetailAPIView.as_view(), name="detail")
    # path('detail/<int:pk>', views.article_detail, name="detail")
]
