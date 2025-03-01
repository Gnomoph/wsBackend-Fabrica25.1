from django.urls import path
from .views import (
    advice_list,
    advice_detail,
    advice_create,
    advice_update,
    advice_delete,
)

urlpatterns = [
    path('', advice_list, name='advice_list'),
    path('advice/<int:pk>/', advice_detail, name='advice_detail'),
    path('advice/create/', advice_create, name='advice_create'),
    path('advice/<int:pk>/update/', advice_update, name='advice_update'),
    path('advice/<int:pk>/delete/', advice_delete, name='advice_delete'),
]
