from django.contrib import admin
from django.urls import path, include

from pets.views import list_pets, show_pet_details, like_pet, create, edit, delete_pet

urlpatterns = [
    path('', list_pets, name='list pet'),
    path('details/<int:pk>/', show_pet_details, name='pet details'),
    path('like/<int:pk>/', like_pet, name='like pet'),
    path('create/', create, name='create pet'),
    path('edit/<int:pk>', edit, name='edit pet'),
    path('delete/<int:pk>', delete_pet, name='delete pet'),

]
