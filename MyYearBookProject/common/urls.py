from django.urls import path
from MyYearBookProject.common import views
from MyYearBookProject.common.views import ShareFunctionalityView

urlpatterns = [
    path('', views.home_page, name='home-page'),
    path('like/<int:photo_id>', views.like_functionality, name='like'),
    path('share/<int:photo_id>/', ShareFunctionalityView.as_view(), name='share-functionality'),
    path('comment/<int:photo_id>', views.comments_functionality, name='comments'),
]
