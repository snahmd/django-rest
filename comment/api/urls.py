from django.urls import path
from comment.api.views import CommentCreateAPIView
app_name = "post"
urlpatterns = [
    path('create', CommentCreateAPIView.as_view(), name='create'),
    
] 