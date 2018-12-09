# from django.conf.urls import url
from django.urls import path
from . import views

app_name = "images"
urlpatterns = [ 
    path("", view=views.Images.as_view(), name="feed"),
    path("<int:image_id>/", view=views.ImageDetail.as_view(), name="ImageDetail"),
    path("<int:image_id>/likes/", view=views.LikeImage.as_view(), name="like_image"),
    path("<int:image_id>/unlikes/", view=views.UnLikeImage.as_view(), name="unlike_image"),
    path("<int:image_id>/comments/", view=views.CommentOnImage.as_view(), name="comment_image"),
    path("<int:image_id>/comments/<int:comment_id>", view=views.ModerateComments.as_view(), name="comment_remove"),
    path("search/", view=views.Search.as_view(), name="search"),    
]


#/image/3/like

# 0 create the url and the view
# 1 take the image_id from the url
# 2 we want to find an image with this image_id
# 3 we want to create a like for that image
# 3/comments/5 
# image-id:3 delete:comment-id:5