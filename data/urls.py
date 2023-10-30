from django.urls import path,include
from . import views

urlpatterns = [

    path('categories', views.GetCategories.as_view()),
    path('categories/<slug>', views.GetCategory.as_view()),
    path('models', views.GetModels.as_view()),
    path('models/<slug>', views.GetModel.as_view()),


]
