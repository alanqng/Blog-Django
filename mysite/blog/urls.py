from django.conf.urls import url, 
from blog import views
from django.urls import path

urlpatterns = [
    path('/',views.PostListView.as_view(), name='post_list'),
    path('about/',views.AboutView.as_view(),name='about'),
    path('post/<pk>',views.DeleteView.as_view(),name='post_detail'),
    path('post/new/', views.CreatePostView.as_view(),name='post_new'),
    path('post/<pk>/edit/', views.PostUpdateView.as_view(),name='post_edit'),
    path('post/<pk>/remove/', views.PostDeleteView.as_view(),name='post_remove'),
    path('drafts/', views.DraftListView.as_view(),name='post_draft_list'),
]