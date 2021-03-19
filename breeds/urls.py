from django.urls import path
from .views import BreedList, BreedDetail

urlpatterns = [
  path('', BreedList.as_view(), name='breed_list'),
  path('<int:pk>', BreedDetail.as_view, name='breed_detail')
]