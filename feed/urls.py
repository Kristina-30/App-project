from django.urls import path
from . import views



app_name = "feed"
urlpatterns = [
    path("", views.HomePage.as_view(), name="feed.index"),
    path("<int:pk>/", views.PostDetailView.as_view(), name="detail"),
    path("new/", views.CreateNewPost.as_view(), name="new_post"),
    path('post/', views.AddPostView.as_view(), name='new_postim'),
    path('profile_view/', views.ViewProfile, name='profile_view'),
    path('profile_view/edit/', views.EditProfile, name='profile_edit'),
    path('profile_view/edit/change_password/', views.change_password, name='change_password'),
    path('profile_view/edit/change_image/', views.change_image, name='change_image'),
    path('search_venues/', views.search_venues, name='search-venues'),
]