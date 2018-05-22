from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('submit/', views.entry, name='entry'),
    path('submit/post/', views.submitEntry, name='submit'),
    path('view/<int:physicianId>/', views.view, name='view'),
]
