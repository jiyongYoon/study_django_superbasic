from django.urls import path

from pybo import views

urlpatterns = [
    path('', views.index),
    path('create/', views.create),
    path('create/answer/<int:question_id>/', views.createAnswer),

    path('read/<int:question_id>/', views.read), # id 가 int 형 타입이 매핑됨을 의미
    path('read/answer/<int:answer_id>/', views.readAnswer),

    path('delete/', views.delete),
    path('delete/answer/', views.deleteAnswer),

    path('update/<int:question_id>/', views.update),
    path('update/answer/<int:answer_id>/', views.updateAnswer),

    path('pybo/', views.pybo_index)
]