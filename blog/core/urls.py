from django.urls import path 
from .views import *
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.decorators import login_required


urlpatterns = [
  
    path('',hello ,name="well"),
    path('createpost',createpost.as_view(),name="createpost"),
    path ('posts',Postlistview.as_view(),name='postslist'),
    path('delete/<int:pk>',postdelete.as_view(),name='postdelete'), 
    path('editpost/<int:pk>',Updatpost.as_view(),name='post_update'),
    path('postdetails/<int:pk>',postDetailview.as_view(),name='postdetails'),
    path('userposts/<str:username>',User_Postlistview.as_view(),name='userposts'),



  

] + static(settings.MEDIA_URL, document_root =settings.MEDIA_ROOT)
  