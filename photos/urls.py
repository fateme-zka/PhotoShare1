from django.urls import path
from .views import gallery, view_photo, add_photo

urlpatterns = [
    path('', gallery, name='gallery'),
    path('add/', add_photo, name='add-photo'),
    path('view/<str:pk>/', view_photo, name='view-photo'),

]
