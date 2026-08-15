from django.urls import path
from .views import ProductosView,ProductosIdView

urlpatterns = [
    path('productos/', ProductosView.as_view(), name="productos"),
    path('productos/<int:id>/', ProductosIdView.as_view()),
]