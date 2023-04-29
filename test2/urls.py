from django.urls import path
from .views import person_list,person_detail, person_create, person_delete, person_update

urlpatterns = [
    path('vse_ludi/', person_list),
    path('person_detail/<int:pk>/',person_detail),
    path('person_create/', person_create),
    path('person_delete/<int:pk>/', person_delete),
    path('person_update/<int:pk>/', person_update),
]
    