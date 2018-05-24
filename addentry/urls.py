from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('submit/', views.entry, name='entry'),
    path('submit/post/', views.submitEntry, name='submit'),
    path('view/<int:physicianId>/', views.view, name='view'),
    path('view/<int:physicianId>/run', views.runRule, name='run'),
    path('view/', views.list.as_view(), name='list'),
    path('edit/', views.ruleList.as_view(), name='rule-list'),
    path('edit/<int:ruleId>', views.editRule, name='edit-rule'),
    path('edit/new/', views.newRule, name='new-rule'),
]
