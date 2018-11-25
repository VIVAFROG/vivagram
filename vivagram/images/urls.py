# from django.conf.urls import url
from django.urls import path
from . import views

app_name = "images"
urlpatterns = [ 
    path("", view=views.Feed.as_view(), name="feed"),
    path("<int:image_id>/like/", view=views.LikeImage.as_view(), name="like_image"),
    path("<int:image_id>/unlike/", view=views.UnLikeImage.as_view(), name="unlike_image"),
    path("<int:image_id>/comments/", view=views.CommentOnImage.as_view(), name="comment_image"),
    path("search/", view=views.Search.as_view(), name="search"),

]


#/image/3/like

# 0 create the url and the view
# 1 take the image_id from the url
# 2 we want to find an image with this image_id
# 3 we want to create a like for that image