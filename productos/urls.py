from django.urls import path
from .views import ProductosView

urlpatterns = [
    path('productos/', ProductosView.as_view(), name="productos"),
    path('productos/<int:id>/', ProductosView.as_view()),
]