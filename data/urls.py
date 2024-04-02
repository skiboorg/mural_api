from django.urls import path,include
from . import views

urlpatterns = [

    path('categories', views.GetCategories.as_view()),
    path('faq', views.GetFaq.as_view()),
    path('categories/<slug>', views.GetCategory.as_view()),
    path('models', views.GetModels.as_view()),
    path('models/<slug>', views.GetModel.as_view()),
    path('callback', views.NewCallback.as_view()),
    path('request', views.NewRequest.as_view()),


]
