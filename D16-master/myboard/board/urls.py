from django.urls import path
from . views import IndexView, AddView, AddCreateView, AddUpdateView, \
    AddDeleteView, ProfilePostDetailsView, comment_update, CommentDelete


urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('<int:pk>/', AddView.as_view(), name='post'),
    path('<int:pk>/details/', ProfilePostDetailsView.as_view(), name='details'),
    path('add/', AddCreateView.as_view(), name='post_create'),
    path('<int:pk>/update/', AddUpdateView.as_view(), name='post_update'),
    path('<int:pk>/delete/', AddDeleteView.as_view(), name='post_delete'),
    path('<int:pk>/comment-update/', comment_update, name='comment_update'),
    path('<int:pk>/comment-delete/', CommentDelete.as_view(), name='comment_delete'),
]