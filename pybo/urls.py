from django.urls import path

from pybo import views

urlpatterns = [
    path('', views.index),
    path('create/', views.create),
    path('read/<int:topic_id>/', views.read), # id 가 int 형 타입이 매핑됨을 의미
    path('delete/', views.delete),
    path('update/<int:topic_id>/', views.update),
    path('pybo/', views.pybo_index)
]