from django.urls import path

from .views import *

urlpatterns = [
    path('main/list/', TicketsApiView.as_view(), name='list'),
    path('main/list/<int:pk>', TicketsApiUpdate.as_view()),
    path('main/comment/', CommentApiView.as_view()),
    path('main/comment/<int:pk>', CommentApiUpdate.as_view()),
    path('main/comment_add/', AddComment.as_view()),
]
