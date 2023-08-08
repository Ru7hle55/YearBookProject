from django.urls import path, include

from MyYearBookProject.photos import views
from MyYearBookProject.photos.views import PhotoDeleteView

urlpatterns = [
    path('add/', views.photo_add, name='photo-add'),
    path('<int:pk>/', include([
        path('', views.photo_details, name='photo-details'),
        path('edit/', views.photo_edit, name='photo-edit'),
        path('delete/', PhotoDeleteView.as_view(), name='photo-delete'),
    ])),
]