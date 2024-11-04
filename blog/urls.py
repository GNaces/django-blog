from django.urls import path
from . import views  # Your view for the post list

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('post/<int:post_id>/like/', views.toggle_like, name='toggle_like'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('<slug:slug>/edit_comment/<int:comment_id>',
         views.comment_edit, name='comment_edit'),
    path('<slug:slug>/delete_comment/<int:comment_id>',
         views.comment_delete, name='comment_delete'),
]