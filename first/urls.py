from django.urls import path
from . import views

urlpatterns = [
    path('',views.Post_list.as_view(),name='list'),
    path('new/',views.Post_new.as_view(),name='new'),
    path('detail/<int:pk>/',views.Post_detail.as_view(),name='detail'),
    path('update/<int:pk>/',views.Post_update.as_view(),name='update'),
    path('delete/<int:pk>/',views.Post_delete.as_view(),name='delete'),
    path('callback/',views.callback,namae='callback'),
]   