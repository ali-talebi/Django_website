from django.urls import path
from . import views  


urlpatterns = [
	path('home/' , views.home , name = 'home' ) ,  
    path('post_list/' , views.post_list , name = 'post_list' ) , 
    path('contact/' , views.forms_contact_me , name = "forms_contact_me" ) , 
    path('about/' , views.about , name = "about" ) ,  
    path('post/details/<slug:slug>/<str:id>' , views.detail_post , name = 'detail_post'  ) , 
]